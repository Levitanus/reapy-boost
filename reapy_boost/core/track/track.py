import reapy_boost
from reapy_boost import reascript_api as RPR
from reapy_boost.core import ReapyObject, ReapyObjectList
from reapy_boost.core.project.project import Project
from reapy_boost.core.audio_accessor import AudioAccessor
from reapy_boost.core.fx.fx import FX
from reapy_boost.core.item.item import Item
from reapy_boost.errors import InsideREAPERError, InvalidObjectError, UndefinedEnvelopeError
import typing as ty


class Track(ReapyObject):
    """
    REAPER Track.

    Parameters
    ----------
    id : str or int
        If str, can either be a ReaScript ID (usually looking like
        ``"(MediaTrack*)0x00000000110A1AD0"``), or a track name. In
        that case, ``project`` must be specified.
        If int, the index of the track. In that case, ``project`` must
        be specified.
    project : Project
        Parent project of the track. Only necessary to retrieve a
        track from its name or index.

    Examples
    --------
    In most cases, accessing tracks is better done directly from
    the parent Project:

    >>> project = reapy_boost.Project()
    >>> project.tracks[0]
    Track("(MediaTrack*)0x00000000110A1AD0")
    >>> project.tracks["PIANO"]  # This is actually the same track
    Track("(MediaTrack*)0x00000000110A1AD0")

    But the same track can also directly be instantiated with:

    >>> reapy_boost.Track(0, project)
    Track("(MediaTrack*)0x00000000110A1AD0")

    or

    >>> reapy_boost.Track("PIANO", project)
    Track("(MediaTrack*)0x00000000110A1AD0")
    """

    def __init__(
        self,
        id: ty.Union[str, int],
        project: ty.Optional[Project] = None
    ) -> None:
        self._project = None
        if isinstance(id, int):  # id is a track index
            id = ty.cast(str, RPR.GetTrack(project.id, id))  # type:ignore
            if id.endswith("0x0000000000000000"):
                raise IndexError('Track index out of range')
            self._project = project
        elif isinstance(id, str) and not id.startswith("(MediaTrack*)"):
            # id is a track name
            name = id
            if project is None:
                raise TypeError(
                    'project has to be specified if instantiated' +
                    f'from track name. Track name: "{name}".'
                )
            track = project._get_track_by_name(name)
            if track is None:
                raise KeyError(f'track with name "{name}" can not be found.')
            id = track.id
            if id.endswith("0x0000000000000000"):
                raise KeyError(name)
            self._project = project
        # id is now a real ReaScript ID
        self.id = id

    @property
    def _args(self) -> ty.Tuple[str]:
        return self.id,

    @classmethod
    def _get_id_from_pointer(cls, pointer: ty.Union[float, str]) -> str:
        return '(MediaTrack*)0x{0:0{1}X}'.format(int(pointer), 16)

    @reapy_boost.inside_reaper()
    def _get_project(self) -> Project:
        """
        Return parent project of track.

        Should only be used internally; one should directly access
        Track.project instead of calling this method.
        """
        for project in reapy_boost.get_projects():
            if self.id in [t.id for t in project.tracks]:
                return project
        raise KeyError('Project can not be found. Maybe track is deleted.')

    def add_audio_accessor(self) -> AudioAccessor:
        """
        Create audio accessor and return it.

        Returns
        -------
        audio_accessor : AudioAccessor
            Audio accessor on track.
        """
        audio_accessor_id = RPR.CreateTrackAudioAccessor(  # type:ignore
            self.id)
        audio_accessor = reapy_boost.AudioAccessor(audio_accessor_id)
        return audio_accessor

    def add_fx(
        self,
        name: str,
        input_fx: bool = False,
        even_if_exists: bool = True
    ) -> FX:
        """
        Add FX to track and return it.

        Parameters
        ----------
        name : str
            FX name.
        input_fx : bool, optional
            Whether the FX should be an input (aka recording) FX or a
            standard FX (default=False). Note that if the track is the
            master track, input_fx=True will create a monitoring FX.
        even_if_exists : bool, optional
            Whether the FX should be added even if there already is an
            instance of the same FX on the track (default=True).

        Returns
        -------
        fx : FX
            New FX on track (or previously existing instance of FX if
            even_if_exists=False).

        Raises
        ------
        ValueError
            If there is no FX with the specified name.
        """
        index = RPR.TrackFX_AddByName(  # type:ignore
            self.id, name, input_fx, 1 - 2 * even_if_exists)
        if index == -1:
            raise ValueError("Can't find FX named {}".format(name))
        fx = reapy_boost.FX(ty.cast(reapy_boost.Track, self), index)
        return fx

    @reapy_boost.inside_reaper()
    def add_item(
        self,
        start: float = 0,
        end: ty.Optional[float] = None,
        length: float = 0
    ) -> Item:
        """
        Create new item on track and return it.

        Parameters
        ----------
        start : float, optional
            New item start in seconds (default=0).
        end : float, optional
            New item end in seconds (default None). If None, `length`
            is used instead.
        length : float, optional
            New item length in seconds (default 0).

        Returns
        -------
        item : Item
            New item on track.
        """
        if end is None:
            end = start + length
        item = reapy_boost.Item(
            RPR.AddMediaItemToTrack(self.id)
        )  # type:ignore
        item.position = start
        item.length = end - start
        return item

    def add_midi_item(
        self,
        start: float = 0,
        end: float = 1,
        quantize: bool = False
    ) -> Item:
        """
        Add empty MIDI item to track and return it.

        Parameters
        ----------
        start : float, optional
            New item start in seconds (or beats if `quantize`=True).
        end : float, optional
            New item end in seconds (or beats if `quantize`=True).
        quantize : bool, optional
            Whether to count time in beats (True) or seconds (False,
            default).
        """
        item_id = RPR.CreateNewMIDIItemInProj(  # type:ignore
            self.id, start, end, quantize)[0]
        item = reapy_boost.Item(item_id)
        return item

    def add_send(self, destination: ty.Optional['Track'] = None):
        """
        Add send to track and return it.

        Parameters
        ----------
        destination : Track or None
            Send destination (default=None). If None, destination is
            set to hardware output.

        Returns
        -------
        send : Send
            New send on track.
        """
        if isinstance(destination, Track):
            destination_id = destination.id
        send_id = RPR.CreateTrackSend(self.id, destination_id)  # type:ignore
        type = "hardware" if destination is None else "send"
        send = reapy_boost.Send(
            ty.cast(reapy_boost.Track, self), send_id, type=type
        )
        return send

    @property
    def automation_mode(self) -> str:  # TODO: make Enum for modes?
        """
        Track automation mode.

        One of the following values:
            "latch"
            "latch preview"
            "read"
            "touch"
            "trim/read"
            "write"

        :type: str
        """
        modes = "trim/read", "read", "touch", "write", "latch", "latch preview"
        automation_mode = modes[
            RPR.GetTrackAutomationMode(  # type:ignore
                self.id
            )]
        return automation_mode

    @automation_mode.setter
    def automation_mode(self, mode: str) -> None:
        """
        Set track automation mode.

        Parameters
        -------
        mode : str
            One of the following values:
                "latch"
                "latch preview"
                "read"
                "touch"
                "trim/read"
                "write"
        """
        modes = "trim/read", "read", "touch", "write", "latch", "latch preview"
        RPR.SetTrackAutomationMode(  # type:ignore
            self.id, modes.index(mode)
        )

    @property
    def color(self) -> ty.Tuple[int, int, int]:  # TODO: make color class?
        """
        Track color in RGB format.

        :type: tuple of int
        """
        native_color = RPR.GetTrackColor(self.id)  # type:ignore
        r, g, b = reapy_boost.rgb_from_native(native_color)
        return r, g, b

    @color.setter
    def color(self, color: ty.Tuple[int, int, int]) -> None:
        """
        Set track color to `color`

        Parameters
        ----------
        color : tuple
            Triplet of integers between 0 and 255 corresponding to RGB
            values.
        """
        native_color = reapy_boost.rgb_to_native(color)
        RPR.SetTrackColor(self.id, native_color)  # type:ignore

    def delete(self) -> None:
        """
        Delete track.
        """
        # TODO: can we verify?
        RPR.DeleteTrack(self.id)  # type:ignore

    @property
    def depth(self) -> int:
        """
        Track depth.

        :type: int
        """
        depth = RPR.GetTrackDepth(self.id)  # type:ignore
        return depth

    @property
    def envelopes(self) -> 'reapy_boost.EnvelopeList':
        """
        List of envelopes on track.

        :type: EnvelopeList
        """
        return reapy_boost.EnvelopeList(ty.cast(reapy_boost.Track, self))

    @classmethod
    def from_GUID(
        cls,
        guid_string: str,
        project: ty.Optional[Project] = None
    ) -> 'reapy_boost.Track':
        """
        Get track from project by GUID string {xyz-...}.

        Parameters
        ----------
        guid_string : str
            can be taken by Track.GUID
        project : Union[Project, str], optional
            if None — current project is used
            if "all" — iterates through all projects (use with care)

        Returns
        -------
        Track

        Raises
        ------
        KeyError
            If no track with the guid string found in project
        """
        if isinstance(project, str):
            if project != "all":
                raise TypeError(
                    'if used string argument — only "all" is accepted'
                )
            return cls._from_GUID_all_projects(guid_string)
        proj = project if project is not None else reapy_boost.Project()
        return proj.get_track_by_guid(guid_string)

    @classmethod
    def _from_GUID_all_projects(cls, guid_string: str) -> 'reapy_boost.Track':
        with reapy_boost.inside_reaper():
            for pr in reapy_boost.get_projects():
                try:
                    return pr.get_track_by_guid(guid_string)
                except (reapy_boost.errors.DistError, KeyError) as e:
                    if str(e).find('KeyError: {'):
                        continue
                    raise e
        raise KeyError(guid_string)

    @property
    def fxs(self) -> 'reapy_boost.FXList':
        """
        List of FXs on track.

        :type: FXList
        """
        fxs = reapy_boost.FXList(ty.cast(reapy_boost.Track, self))
        return fxs

    def get_info_string(self, param_name: str) -> str:
        return RPR.GetSetMediaTrackInfo_String(  # type:ignore
            self.id, param_name, "", False)[3]

    def get_info_value(self, param_name: str) -> float:
        value = RPR.GetMediaTrackInfo_Value(  # type:ignore
            self.id, param_name)
        return value

    @property
    def GUID(self) -> str:
        """
        Track's GUID string {xyz-...}.

        :type: str
        """
        return self.get_info_string("GUID")

    @GUID.setter
    def GUID(self, guid_string: str) -> None:
        self.set_info_string("GUID", guid_string)

    @property
    def has_valid_id(self):
        """
        Whether ReaScript ID is still valid.

        For instance, if track has been deleted, ID will not be valid
        anymore.

        :type: bool
        """
        return self._has_valid_id_inside()

    @reapy_boost.inside_reaper()
    def _has_valid_id_inside(self) -> bool:
        pointer, name = self._get_pointer_and_name()
        if self._project is None:
            return any(
                RPR.ValidatePtr2(p.id, pointer, name)  # type:ignore
                for p in reapy_boost.get_projects()
            )
        return bool(
            RPR.ValidatePtr2(  # type:ignore
                self.project.id, pointer, name
            )
        )

    @property
    def icon(self) -> str:
        """
        Track icon.

        Full filename, or relative to resource_path/data/track_icons.

        :type: str
        """
        return self.get_info_string("P_ICON")

    @icon.setter
    def icon(self, filename: str) -> None:
        self.set_info_string("P_ICON", filename)

    @property
    def index(self) -> ty.Optional[int]:
        """Track index in GUI (0-based).

        Will be ``None`` for master track.

        :type: int or None

        Raises
        ------
        InvalidObjectError
            When track does not exist in REAPER.
        """
        index = int(self.get_info_value('IP_TRACKNUMBER')) - 1
        if index >= 0:
            return index
        if index == -1:
            raise InvalidObjectError(self)

    @property
    def instrument(self) -> ty.Optional['reapy_boost.FX']:
        """
        First instrument FX on track if it exists, else None.

        :type: FX or None
        """
        fx_index = RPR.TrackFX_GetInstrument(self.id)  # type:ignore
        instrument = None if fx_index == -1 else reapy_boost.FX(self, fx_index)
        return instrument

    @property
    def items(self) -> ty.List['reapy_boost.Item']:
        """
        List of items on track.

        :type: list of Item
        """
        return self._items_inside()

    @reapy_boost.inside_reaper()
    def _items_inside(self) -> ty.List['reapy_boost.Item']:
        n_items = RPR.CountTrackMediaItems(self.id)  # type:ignore
        item_ids = [
            RPR.GetTrackMediaItem(  # type:ignore
                self.id, i
            ) for i in range(n_items)
        ]
        return list(map(reapy_boost.Item, item_ids))

    @property
    def is_muted(self) -> bool:
        """
        Whether track is muted.

        Can be manually set to change track state.
        """
        return bool(self.get_info_value("B_MUTE"))

    @is_muted.setter
    def is_muted(self, muted: bool) -> None:
        if muted:
            self.mute()
        else:
            self.unmute()

    @property
    def is_selected(self) -> bool:
        """
        Whether track is selected.

        :type: bool
        """
        is_selected = bool(RPR.IsTrackSelected(  # type:ignore
            self.id
        ))
        return is_selected

    @is_selected.setter
    def is_selected(self, selected: bool) -> None:
        """
        Select or unselect track.

        Parameters
        ----------
        selected : bool
            Whether to select or unselect track.
        """
        if selected:
            self.select()
        else:
            self.unselect()

    @property
    def is_solo(self) -> bool:
        """
        Whether track is solo.

        Can be manually set to change track state.
        """
        return bool(self.get_info_value("I_SOLO"))

    @is_solo.setter
    def is_solo(self, solo: bool) -> None:
        if solo:
            self.solo()
        else:
            self.unsolo()

    def make_only_selected_track(self) -> None:
        """
        Make track the only selected track in parent project.
        """
        RPR.SetOnlyTrackSelected(self.id)  # type:ignore

    def midi_hash(self, notes_only: bool = False) -> str:
        """Get hash of MIDI-data to compare with later.

        Parameters
        ----------
        notes_only : bool, (False by default)
            count only notes if True

        Returns
        -------
        str
        """
        return RPR.MIDI_GetTrackHash(  # type:ignore
            self.id, notes_only, 'hash', 1024**2)[3]

    @property
    def midi_note_names(self) -> ty.List[str]:
        with reapy_boost.inside_reaper():
            names = [
                RPR.GetTrackMIDINoteName(  # type:ignore
                    self.index, i, 0
                ) for i in range(128)
            ]
            return names
        raise InsideREAPERError('Contex manager exited without value.')

    @reapy_boost.inside_reaper()
    def mute(self) -> None:
        """Mute track (do nothing if track is already muted)."""
        if not self.is_muted:
            self.toggle_mute()

    @property
    def n_envelopes(self) -> int:
        """
        Number of envelopes on track.

        :type: int
        """
        n_envelopes = RPR.CountTrackEnvelopes(self.id)  # type:ignore
        return n_envelopes

    @property
    def n_fxs(self) -> int:
        """
        Number of FXs on track.

        :type: int
        """
        n_fxs = RPR.TrackFX_GetCount(self.id)  # type:ignore
        return n_fxs

    @property
    def n_hardware_sends(self) -> int:
        """
        Number of hardware sends on track.

        :type: int
        """
        n_hardware_sends = RPR.GetTrackNumSends(self.id, 1)  # type:ignore
        return n_hardware_sends

    @property
    def n_items(self) -> int:
        """
        Number of items on track.

        :type: int
        """
        n_items = RPR.CountTrackMediaItems(self.id)  # type:ignore
        return n_items

    @property
    def n_receives(self) -> int:
        n_receives = RPR.GetTrackNumSends(self.id, -1)  # type:ignore
        return n_receives

    @property
    def n_sends(self) -> int:
        n_sends = RPR.GetTrackNumSends(self.id, 0)  # type:ignore
        return n_sends

    @property
    def name(self) -> str:
        """
        Track name.

        Name is "MASTER" for master track, "Track N" if track has no
        name.

        :type: str
            Track name .
        """
        _, _, name, _ = RPR.GetTrackName(self.id, "", 2048)  # type:ignore
        return name

    @name.setter
    def name(self, track_name: str) -> None:
        self.set_info_string("P_NAME", track_name)

    @property
    def parent_track(self) -> ty.Optional['reapy_boost.Track']:
        """
        Parent track, or None if track has none.

        :type: Track or NoneType
        """
        parent = reapy_boost.Track(RPR.GetParentTrack(self.id))  # type:ignore
        if not parent._is_defined:
            parent = None
        return parent

    @property
    def project(self) -> 'reapy_boost.Project':
        """
        Track parent project.

        :type: Project
        """
        if self._project is None:
            self._project = self._get_project()
        return self._project

    @property
    def receives(self):
        return self._recieves_inside()

    @reapy_boost.inside_reaper()
    def _recieves_inside(self) -> ty.List['reapy_boost.Send']:
        return [
            reapy_boost.Send(
                ty.cast(reapy_boost.Track, self), i, type="receive"
            ) for i in range(self.n_receives)
        ]

    def select(self):
        """
        Select track.
        """
        RPR.SetTrackSelected(self.id, True)  # type:ignore

    @property
    def sends(self):
        return self._send_inside()

    @reapy_boost.inside_reaper()
    def _send_inside(self) -> ty.List['reapy_boost.Send']:
        return [
            reapy_boost.Send(reapy_boost.Track(self.id), i, type="send")
            for i in range(self.n_sends)
        ]

    def set_info_string(self, param_name: str, param_string: str) -> None:
        RPR.GetSetMediaTrackInfo_String(  # type:ignore
            self.id, param_name, param_string, True)

    def set_info_value(self, param_name: str, param_value: float) -> None:
        RPR.SetMediaTrackInfo_Value(  # type:ignore
            self.id, param_name, param_value)

    @reapy_boost.inside_reaper()
    def solo(self) -> None:
        """Solo track (do nothing if track is already solo)."""
        if not self.is_solo:
            self.toggle_solo()

    @reapy_boost.inside_reaper()
    def toggle_mute(self) -> None:
        """Toggle mute on track."""
        selected_tracks = self.project.selected_tracks
        self.make_only_selected_track()
        self.project.perform_action(40280)
        self.project.selected_tracks = selected_tracks

    @reapy_boost.inside_reaper()
    def toggle_solo(self) -> None:
        """Toggle solo on track."""
        selected_tracks = self.project.selected_tracks
        self.make_only_selected_track()
        self.project.perform_action(7)
        self.project.selected_tracks = selected_tracks

    @reapy_boost.inside_reaper()
    def unmute(self) -> None:
        """Unmute track (do nothing if track is not muted)."""
        if self.is_muted:
            self.toggle_mute()

    def unselect(self) -> None:
        """
        Unselect track.
        """
        RPR.SetTrackSelected(self.id, False)  # type:ignore

    @reapy_boost.inside_reaper()
    def unsolo(self) -> None:
        """Unsolo track (do nothing if track is not solo)."""
        if self.is_solo:
            self.toggle_solo()

    @property
    def visible_fx(self) -> ty.Optional['reapy_boost.FX']:
        """
        Visible FX in FX chain if any, else None.

        :type: FX or NoneType
        """
        with reapy_boost.inside_reaper():
            return self.fxs[
                RPR.TrackFX_GetChainVisible(  # type:ignore
                    self.id
                )]


TrackListKeyType = ty.Union[slice, int]


class TrackList(ReapyObjectList):
    """
    Container for a project's track list.

    Examples
    --------
    >>> tracks = project.tracks
    >>> len(tracks)
    4
    >>> tracks[0].name
    'Kick'
    >>> for track in tracks:
    ...     print(track.name)
    ...
    'Kick'
    'Snare'
    'Hi-hat'
    'Cymbal"
    """

    def __init__(self, parent: 'reapy_boost.Project') -> None:
        """
        Create track list.

        Parameters
        ----------
        parent : Project
            Parent project.
        """
        self.parent = parent

    @reapy_boost.inside_reaper()
    def __delitem__(self, key: TrackListKeyType) -> None:
        tracks = self[key] if isinstance(key, slice) else [self[key]]
        for track in tracks:
            track.delete()

    @ty.overload
    def __getitem__(self, key: slice) -> ty.List['reapy_boost.Track']:
        ...

    @ty.overload
    def __getitem__(self, key: int) -> 'reapy_boost.Track':
        ...

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self._get_items_from_slice(key)
        return reapy_boost.Track(key, self.parent)

    def __iter__(self):
        tracks = self[:]  # Only cost one distant call
        for track in tracks:
            yield track

    def __len__(self):
        return self.parent.n_tracks

    @property
    def _args(self):
        return self.parent,

    @reapy_boost.inside_reaper()
    def _get_items_from_slice(self,
                              slice: slice) -> ty.List['reapy_boost.Track']:
        indices = range(*slice.indices(len(self)))
        return [self[i] for i in indices]
        # return [self[i] for i in indices]
