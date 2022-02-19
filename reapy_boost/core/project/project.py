"""Defines class Project."""

import pickle
import codecs
import os
from typing import List, Optional, Tuple, TypedDict, Union, cast, overload

import reapy_boost
from reapy_boost import reascript_api as RPR
from reapy_boost.core import ReapyObject
from reapy_boost.errors import RedoError, UndoError


class MeasureInfo(TypedDict):
    """
    start: float
        in quarter notes
    end: float
        in quarter notes
    num: int
        numenator of time signature (e.g. 3 in 3/8)
    denom: int
        denominator of time signature (e.g. 8 in 3/8)
    bpm: float
    """
    start: float
    end: float
    num: int
    denom: int
    bpm: float


class Project(ReapyObject):
    """REAPER project."""

    def __init__(self, id: Optional[Union[str, int]] = None, index: int = -1):
        """
        Build project either by ID or index.

        Parameters
        ----------
        id : None, str or int, optional
            Project identifier.
            When None (default), `index is used instead.
            An integer is interpreted as the project index in GUI.
            A string starting with '(ReaProject*)0x' is interpreted
            as a ReaScript identifier.
            Otherwise, `id` is the project name. In that case, the .rpp
            extension is optional.
        index : int, optional
            Project index in GUI (default=-1, corresponds to current
            project).
        """
        if isinstance(id, int):
            id, index = None, cast(int, id)
        if id is None:
            id = cast(str, RPR.EnumProjects(index, None, 0)[0])  # type:ignore
        if not id.startswith('(ReaProject*)0x'):
            id = Project._from_name(id).id
        self.id: str = id
        self._filename = None

    def __eq__(self, other: object) -> bool:
        if hasattr(other, 'id'):
            return self.id == other.id
        return False

    @property
    def _args(self) -> Tuple[str]:
        return self.id,

    @staticmethod
    def _from_name(name: str) -> 'Project':
        """Return project with corresponding name.

        Parameters
        ----------
        name : str
            Project file name. Including the extension ('.rpp')
            is optional.

        Returns
        -------
        Project

        Raises
        ------
        NameError
            If no project with the corresponding name is open.
        """
        if not name.lower().endswith('.rpp'):
            name += '.rpp'
        with reapy_boost.inside_reaper():
            for project in reapy_boost.get_projects():
                project_name = project.name[:-4] + '.rpp'
                if project_name == name:
                    return project
        raise NameError('"{}" is not currently open.'.format(name))

    @reapy_boost.inside_reaper()
    def _get_track_by_name(self, name: str) -> 'reapy_boost.Track':
        """Return first track with matching name."""
        for track in self.tracks:
            if track.name == name:
                return track
        raise KeyError(name)

    def add_marker(
        self,
        position: float,
        name: str = "",
        color: Union[int, Tuple[int, int, int]] = 0
    ) -> 'reapy_boost.Marker':
        """
        Create new marker and return its index.

        Parameters
        ----------
        position : float
            Marker position in seconds.
        name : str, optional
            Marker name.
        color : int or tuple of int, optional
            Marker color. Integers correspond to REAPER native colors.
            Tuple must be RGB triplets of integers between 0 and 255.

        Returns
        -------
        marker : reapy_boost.Marker
            New marker.

        Notes
        -----
        If a marker with the same position and name already exists, no
        new marker will be created, and the existing marker index will
        be returned.
        """
        if isinstance(color, tuple):
            color = reapy_boost.rgb_to_native(color) | 0x1000000
        marker_id = RPR.AddProjectMarker2(  # type:ignore
            self.id, False, position, 0, name, -1, color
        )
        marker = reapy_boost.Marker(self, index=marker_id)
        return marker

    def add_region(
        self,
        start: float,
        end: float,
        name: str = "",
        color: Union[int, Tuple[int, int, int]] = 0
    ) -> 'reapy_boost.Region':
        """
        Create new region and return its index.

        Parameters
        ----------
        start : float
            Region start in seconds.
        end : float
            Region end in seconds.
        name : str, optional
            Region name.
        color : int or tuple of int, optional
            Region color. Integers correspond to REAPER native colors.
            Tuple must be RGB triplets of integers between 0 and 255.

        Returns
        -------
        region : reapy_boost.Region
            New region.
        """
        if isinstance(color, tuple):
            color = reapy_boost.rgb_to_native(color) | 0x1000000
        region_id = RPR.AddProjectMarker2(  # type:ignore
            self.id, True, start, end, name, -1, color
        )
        region = reapy_boost.Region(self, index=region_id)
        return region

    @reapy_boost.inside_reaper()
    def add_track(self, index: int = 0, name: str = "") -> 'reapy_boost.Track':
        """
        Add track at a specified index.

        Parameters
        ----------
        index : int
            Index at which to insert track.
        name : str, optional
            Name of created track.

        Returns
        -------
        track : Track
            New track.
        """
        n_tracks = self.n_tracks
        index = max(-n_tracks, min(index, n_tracks))
        if index < 0:
            index = index % n_tracks
        with self.make_current_project():
            RPR.InsertTrackAtIndex(index, True)  # type:ignore
        track = self.tracks[index]
        track.name = name
        return track

    @property
    def any_track_solo(self) -> bool:
        """
        Test whether any track is soloed in project.

        Returns
        -------
        any_track_solo : bool
            Whether any track is soloed in project.
        """
        any_track_solo = bool(RPR.AnyTrackSolo(self.id))  # type:ignore
        return any_track_solo

    def beats_to_measures(self, beats: float) -> Tuple[int, float, float]:
        """Get measure from quarter notes.

        Parameters
        ----------
        beats : float
            quarter notes from start

        Returns
        -------
        Tuple[int, float, float]
            measure number: int
            measure start in quarter notes: float
            measure end in quarter notes: float
        """
        (m, _, _, m_start, m_end
         ) = RPR.TimeMap_QNToMeasures(  # type:ignore
             self.id, beats, 0, 0
         )
        return m, m_start, m_end

    def beats_to_time(self, beats: float) -> float:
        """
        Convert beats to time in seconds.

        Parameters
        ----------
        beats : float
            Time in beats

        Returns
        -------
        time : float
            Converted time in seconds.

        See also
        --------
        Project.time_to_beats
        """
        time = RPR.TimeMap2_QNToTime(self.id, beats)  # type:ignore
        return time

    def begin_undo_block(self) -> None:
        """
        Start a new undo block.
        """
        RPR.Undo_BeginBlock2(self.id)  # type:ignore

    @property
    def bpi(self) -> int:
        """
        Return project BPI (numerator of time signature).

        Returns
        -------
        bpi : int
            Numerator of time signature.
        """
        return self.time_signature[1]

    @property
    def bpm(self) -> float:
        """
        Project BPM (beats per minute).

        :type: float
        """
        return self.time_signature[0]

    @bpm.setter
    def bpm(self, bpm: float) -> None:
        """
        Set project BPM (beats per minute).

        Parameters
        ----------
        bpm : float
            Tempo in beats per minute.
        """
        RPR.SetCurrentBPM(self.id, bpm, True)  # type:ignore

    @property
    def buffer_position(self) -> float:
        """
        Position of next audio block being processed in seconds.

        :type: float

        See also
        --------
        Project.play_position
            Latency-compensated actual-what-you-hear position.
        """
        return RPR.GetPlayPosition2Ex(self.id)  # type:ignore

    @reapy_boost.inside_reaper()
    def bypass_fx_on_all_tracks(self, bypass: bool = True) -> None:
        """
        Bypass or un-bypass FX on all tracks.

        Parameters
        ----------
        bypass : bool
            Whether to bypass or un-bypass FX.
        """
        with self.make_current_project():
            RPR.BypassFxAllTracks(bypass)  # type:ignore

    @property
    def can_redo(self) -> bool:
        """
        Whether redo is possible.

        :type: bool
        """
        try:
            RPR.Undo_CanRedo2(self.id)  # type:ignore
            can_redo = True
        except AttributeError:  # Bug in ReaScript API
            can_redo = False
        return can_redo

    @property
    def can_undo(self) -> bool:
        """
        Whether undo is possible.

        :type: bool
        """
        try:
            RPR.Undo_CanUndo2(self.id)  # type:ignore
            can_undo = True
        except AttributeError:  # Bug in ReaScript API
            can_undo = False
        return can_undo

    def close(self) -> None:
        """Close project and its correspondig tab."""
        self._filename = os.path.join(self.path, self.name)
        with self.make_current_project():
            reapy_boost.perform_action(40860)

    @property
    def cursor_position(self) -> float:
        """
        Edit cursor position in seconds.

        :type: float
        """
        position = RPR.GetCursorPositionEx(self.id)  # type:ignore
        return position

    @cursor_position.setter
    def cursor_position(self, position: float) -> None:
        """
        Set edit cursor position.

        Parameters
        ----------
        position : float
            New edit cursor position in seconds.
        """
        RPR.SetEditCurPos(position, True, True)  # type:ignore

    @reapy_boost.inside_reaper()
    def disarm_rec_on_all_tracks(self) -> None:
        """
        Disarm record on all tracks.
        """
        with self.make_current_project():
            RPR.ClearAllRecArmed()  # type:ignore

    def end_undo_block(self, description: str = "", flags: int = -1) -> None:
        """
        End undo block.

        Parameters
        ----------
        description : str
            Undo block description.
        flags : int
            1: track configurations
            2: track FX
            4: track items
            8: project states
            16: freeze states
        """
        RPR.Undo_EndBlock2(self.id, description, flags)  # type:ignore

    @property
    def focused_fx(self) -> Optional['reapy_boost.FX']:
        """
        FX that has focus if any, else None.

        :type: FX or NoneType
        """
        return self._focused_fx_inside()

    @reapy_boost.inside_reaper()
    def _focused_fx_inside(self) -> Optional['reapy_boost.FX']:
        if not self.is_current_project:
            return None
        res = RPR.GetFocusedFX(0, 0, 0)  # type:ignore
        if not res[0]:
            return None
        if res[1] == 0:
            track = self.master_track
        else:
            track = self.tracks[res[1] - 1]
        if res[0] == 1:  # Track FX
            return track.fxs[res[3]]
        # Take FX
        item = track.items[res[2]]
        take = item.takes[res[3] // 2**16]
        return take.fxs[res[3] % 2**16]

    def get_info_string(self, param_name: str) -> str:
        """
        Parameters
        ----------
        param_name : str
            MARKER_GUID:X : get the GUID (unique ID) of the marker or region
                with index X, where X is the index passed to
                EnumProjectMarkers, not necessarily the displayed number
            RECORD_PATH :
                recording directory -- may be blank or a relative path,
                to get the effective path see GetProjectPathEx()
            RENDER_FILE : render directory
            RENDER_PATTERN : render file name (may contain wildcards)
            RENDER_FORMAT : base64-encoded sink configuration
                (see project files, etc). Callers can also pass a simple
                4-byte string (non-base64-encoded), e.g. "evaw" or "l3pm",
                to use default settings for that sink type.
            RENDER_FORMAT2 : base64-encoded secondary sink configuration.
                Callers can also pass a simple 4-byte string (non-base64-encoded),
                e.g. "evaw" or "l3pm", to use default settings for
                that sink type, or "" to disable secondary render.
                Formats available on this machine:
                "wave" "aiff" "iso " "ddp " "flac" "mp3l" "oggv" "OggS"
                "FFMP" "GIF " "LCF " "wvpk"
        """
        _, _, _, result, _ = RPR.GetSetProjectInfo_String(  # type:ignore
            self.id, param_name, 'valuestrNeedBig', False
        )
        return result  # type:ignore

    def get_info_value(self, param_name: str) -> float:
        """
        Parameters
        ----------
        param_name : str
            RENDER_SETTINGS : &(1|2)=0:master mix, &1=stems+master mix,
                &2=stems only, &4=multichannel tracks to multichannel files,
                &8=use render matrix, &16=tracks with only mono media
                to mono files, &32=selected media items,
                &64=selected media items via master
            RENDER_BOUNDSFLAG : 0=custom time bounds, 1=entire project,
                2=time selection, 3=all project regions,
                4=selected media items, 5=selected project regions
            RENDER_CHANNELS : number of channels in rendered file
            RENDER_SRATE : sample rate of rendered file
                (or 0 for project sample rate)
            RENDER_STARTPOS : render start time when RENDER_BOUNDSFLAG=0
            RENDER_ENDPOS : render end time when RENDER_BOUNDSFLAG=0
            RENDER_TAILFLAG : apply render tail setting when rendering:
                &1=custom time bounds, &2=entire project, &4=time selection,
                &8=all project regions, &16=selected media items,
                &32=selected project regions
            RENDER_TAILMS : tail length in ms to render
                (only used if RENDER_BOUNDSFLAG and RENDER_TAILFLAG are set)
            RENDER_ADDTOPROJ : 1=add rendered files to project
            RENDER_DITHER : &1=dither, &2=noise shaping, &4=dither stems,
                &8=noise shaping on stems
            PROJECT_SRATE : samplerate (ignored unless PROJECT_SRATE_USE set)
            PROJECT_SRATE_USE : set to 1 if project samplerate is used
        """
        return RPR.GetSetProjectInfo(  # type:ignore
            self.id, param_name, 0, False
        )

    def get_play_rate(self, position: float) -> float:
        """
        Return project play rate at a given position.

        Parameters
        ----------
        position : float
            Position in seconds.

        Returns
        -------
        play_rate : float
            Play rate at the given position.

        See also
        --------
        Project.play_rate
            Project play rate at the current position.
        """
        play_rate = RPR.Master_GetPlayRateAtTime(  # type:ignore
            position, self.id)
        return play_rate  # type:ignore

    def get_selected_item(self, index: int) -> 'reapy_boost.Item':
        """
        Return index-th selected item.

        Parameters
        ----------
        index : int
            Item index.

        Returns
        -------
        item : Item
            index-th selected item.
        """
        item_id = RPR.GetSelectedMediaItem(self.id, index)  # type:ignore
        item = reapy_boost.Item(item_id)
        return item

    def get_selected_track(self, index: int) -> 'reapy_boost.Track':
        """
        Return index-th selected track.

        Parameters
        ----------
        index : int
            Track index.

        Returns
        -------
        track : Track
            index-th selected track.
        """
        track_id = RPR.GetSelectedTrack(self.id, index)  # type:ignore
        track = reapy_boost.Track(track_id)
        return track

    @reapy_boost.inside_reaper()
    def get_track_by_guid(self, guid_string: str) -> 'reapy_boost.Track':
        """
        Get track with giver GUID string {xyz-...}.

        Parameters
        ----------
        guid_string : str

        Returns
        -------
        Track

        Raises
        ------
        KeyError
            If no track with the guid string found in project
        """
        for tr in self.tracks:
            if guid_string == tr.GUID:
                return tr
        raise KeyError(guid_string)

    def get_ext_state(self,
                      section: str,
                      key: str,
                      pickled: bool = False) -> Union[str, object]:
        """
        Return external state of project.

        Parameters
        ----------
        section : str
        key : str
        pickled: bool
            Whether data was pickled or not.

        Returns
        -------
        value : str
            If key or section does not exist an empty string is returned.
        """
        value = RPR.GetProjExtState(  # type:ignore
            self.id,
            section,
            key,
            "",
            2**31 - 1
        )[4]
        if value and pickled:
            value = pickle.loads(codecs.decode(value.encode(), "base64"))
        return value  # type:ignore

    def glue_items(self, within_time_selection: bool = False) -> None:
        """
        Glue items (action shortcut).

        Parameters
        ----------
        within_time_selection : bool
            If True, glue items within time selection.
        """
        action_id = 41588 if within_time_selection else 40362
        self.perform_action(action_id)

    @property
    def has_valid_id(self) -> bool:
        """
        Whether ReaScript ID is still valid.

        For instance, if project has been closed, ID will not be valid
        anymore.

        :type: bool
        """
        return bool(
            RPR.ValidatePtr(  # type:ignore
                *self._get_pointer_and_name()
            )
        )

    @property
    def is_dirty(self) -> bool:
        """
        Whether project is dirty (i.e. needing save).

        :type: bool
        """
        is_dirty = RPR.IsProjectDirty(self.id)  # type:ignore
        return bool(is_dirty)

    @property
    def is_current_project(self) -> bool:
        """
        Whether project is current project.

        :type: bool
        """
        is_current = self == Project()
        return is_current

    @property
    def is_paused(self) -> bool:
        """
        Return whether project is paused.

        :type: bool
        """
        return bool(RPR.GetPlayStateEx(self.id) & 2)  # type:ignore

    @property
    def is_playing(self) -> bool:
        """
        Return whether project is playing.

        :type: bool
        """
        return bool(RPR.GetPlayStateEx(self.id) & 1)  # type:ignore

    @property
    def is_recording(self) -> bool:
        """
        Return whether project is recording.

        :type: bool
        """
        return bool(RPR.GetPlayStateEx(self.id) & 4)  # type:ignore

    @property
    def is_stopped(self) -> bool:
        """
        Return whether project is stopped.

        :type: bool
        """
        return self._is_stopped_inside()

    @reapy_boost.inside_reaper()
    def _is_stopped_inside(self) -> bool:
        return not self.is_playing and not self.is_paused

    @property
    def items(self) -> List['reapy_boost.Item']:
        """
        List of items in project.

        :type: list of Item
        """
        return self._items_inside()

    @reapy_boost.inside_reaper()
    def _items_inside(self) -> List['reapy_boost.Item']:
        n_items = self.n_items
        item_ids = [
            RPR.GetMediaItem(  #type:ignore
                self.id, i
            ) for i in range(n_items)
        ]
        return list(map(reapy_boost.Item, item_ids))

    @property
    def length(self) -> float:
        """
        Project length in seconds.

        :type: float
        """
        length = RPR.GetProjectLength(self.id)  #type:ignore
        return length

    @property
    def last_touched_fx(
        self
    ) -> Tuple[Optional['reapy_boost.FX'], Optional[int]]:
        """
        Last touched FX and corresponding parameter index.

        :type: FX, int or NoneType, NoneType

        Notes
        -----
        Only Track FX are detected by this property. If last touched
        FX is a Take FX, this property is ``(None, None)``.

        Examples
        --------
        >>> fx, index = project.last_touched_fx
        >>> fx.name
        'VSTi: ReaSamplOmatic5000 (Cockos)'
        >>> fx.params[index].name
        "Volume"
        """
        return self._last_touched_fx_inside()

    @reapy_boost.inside_reaper()
    def _last_touched_fx_inside(
        self
    ) -> Tuple[Optional['reapy_boost.FX'], Optional[int]]:
        if not self.is_current_project:
            fx, index = None, None
        else:
            res = RPR.GetLastTouchedFX(0, 0, 0)
            if not res[0]:
                fx, index = None, None
            else:
                if res[1]:
                    track = self.tracks[res[1] - 1]
                else:
                    track = self.master_track
                fx, index = track.fxs[res[2]], res[3]
        return fx, index

    @property
    def loop_points(self) -> Tuple[float, float]:
        _, _, _, startOut, endOut, _ = RPR.GetSet_LoopTimeRange2(  # type:ignore
            self.id, False, False, False, False, False
        )
        return startOut, endOut

    @loop_points.setter
    def loop_points(self, points: Tuple[float, float]) -> None:
        RPR.GetSet_LoopTimeRange2(  # type:ignore
            self.id, True, True, points[0], points[1], False
        )

    def make_current_project(self) -> '_MakeCurrentProject':
        """
        Set project as current project.

        Can also be used as a context manager to temporarily set
        the project as current project and then go back to the original
        situation.

        Examples
        --------
        >>> p1 = reapy_boost.Project()  # current project
        >>> p2 = reapy_boost.Project(1)  # other project
        >>> p2.make_current_project()  # now p2 is current project
        >>> with p1.make_current_project():
        ...     do_something()  # current project is temporarily p1
        >>> # and p2 is current project again
        """
        return _MakeCurrentProject(self)

    def mark_dirty(self) -> None:
        """
        Mark project as dirty (i.e. needing save).
        """
        RPR.MarkProjectDirty(self.id)  # type:ignore

    @property
    def markers(self) -> List['reapy_boost.Marker']:
        """
        List of project markers.

        :type: list of reapy_boost.Marker
        """
        return self._markers_inside()

    @reapy_boost.inside_reaper()
    def _markers_inside(self) -> List['reapy_boost.Marker']:
        ids = [
            RPR.EnumProjectMarkers2(  # type:ignore
                self.id, i, 0, 0, 0, 0, 0
            ) for i in range(self.n_regions + self.n_markers)
        ]
        return [
            reapy_boost.Marker(self, index=i[7], enum_index=i[0] - 1)
            for i in ids if not i[3]
        ]

    @property
    def master_track(self) -> 'reapy_boost.Track':
        """
        Project master track.

        :type: Track
        """
        track_id = RPR.GetMasterTrack(self.id)  # type:ignore
        master_track = reapy_boost.Track(track_id)
        return master_track

    def measure_info(self, measure: int) -> MeasureInfo:
        """Information about measure.

        Parameters
        ----------
        measure : int
            number from the project start

        Returns
        -------
        MeasureInfo:
            start: float
                in quarter notes
            end: float
                in quarter notes
            num: int
                numenator of time signature (e.g. 3 in 3/8)
            denom: int
                denominator of time signature (e.g. 8 in 3/8)
            bpm: float
        """
        (_, _, _, start, end, num, denom,
            bpm) = RPR.TimeMap_GetMeasureInfo(  # type:ignore
            self.id, measure-1, 0, 0, 0, 0, 0)
        return MeasureInfo(
            start=cast(float, start),
            end=cast(float, end),
            num=int(num),
            denom=int(denom),
            bpm=cast(float, bpm),
        )

    @reapy_boost.inside_reaper()
    def mute_all_tracks(self, mute: bool = True) -> None:
        """
        Mute or unmute all tracks.

        Parameters
        ----------
        mute : bool, optional
            Whether to mute or unmute all tracks (default=True).

        See also
        --------
        Project.unmute_all_tracks
        """
        with self.make_current_project():
            RPR.MuteAllTracks(mute)  # type:ignore

    @property
    def n_items(self) -> int:
        """
        Number of items in project.

        :type: int
        """
        n_items = RPR.CountMediaItems(self.id)  #type:ignore
        return cast(int, n_items)

    @property
    def n_markers(self) -> int:
        """
        Number of markers in project.

        :type: int
        """
        n_markers = RPR.CountProjectMarkers(self.id, 0, 0)[2]  #type:ignore
        return cast(int, n_markers)

    @property
    def n_regions(self) -> int:
        """
        Number of regions in project.

        :type: int
        """
        n_regions = RPR.CountProjectMarkers(self.id, 0, 0)[3]  #type:ignore
        return cast(int, n_regions)

    @property
    def n_selected_items(self) -> int:
        """
        Number of selected media items.

        :type: int
        """
        n_items = RPR.CountSelectedMediaItems(self.id)  #type:ignore
        return cast(int, n_items)

    @property
    def n_selected_tracks(self) -> int:
        """
        Number of selected tracks in project (excluding master).

        :type: int
        """
        n_tracks = RPR.CountSelectedTracks2(self.id, False)  #type:ignore
        return cast(int, n_tracks)

    @property
    def n_tempo_markers(self) -> int:
        """
        Number of tempo/time signature markers in project.

        :type: int
        """
        n_tempo_markers = RPR.CountTempoTimeSigMarkers(self.id)  #type:ignore
        return cast(int, n_tempo_markers)

    @property
    def n_tracks(self) -> int:
        """
        Number of tracks in project.

        :type: int
        """
        n_tracks = RPR.CountTracks(self.id)  #type:ignore
        return cast(int, n_tracks)

    @property
    def name(self) -> str:
        """
        Project name.

        :type: str
        """
        _, name, _ = RPR.GetProjectName(self.id, "", 2048)  #type:ignore
        return cast(str, name)

    def open(self, in_new_tab: bool = False) -> None:
        """
        Open project, if it was closed by Project.close.

        Parameters
        ----------
        in_new_tab : bool, optional
            whether should be opened in new tab

        Raises
        ------
        RuntimeError
            If hasn't been closed by Project.close yet
        """
        if self._filename is None:
            raise RuntimeError("project hasn't been closed")
        self.id = reapy_boost.open_project(self._filename, in_new_tab).id

    def pause(self) -> None:
        """
        Hit pause button.
        """
        RPR.OnPauseButtonEx(self.id)  #type:ignore

    @property
    def path(self) -> str:
        """
        Project path.

        :type: str
        """
        _, path, _ = RPR.GetProjectPathEx(self.id, "", 2048)  #type:ignore
        return cast(str, path)

    def perform_action(self, action_id: int) -> None:
        """
        Perform action with ID `action_id` in the main Actions section.

        Parameters
        ----------
        action_id : int
            Action ID in the main Actions section.
        """
        RPR.Main_OnCommandEx(action_id, 0, self.id)  #type:ignore

    def play(self) -> None:
        """
        Hit play button.
        """
        RPR.OnPlayButtonEx(self.id)  #type:ignore

    @property
    def play_position(self) -> float:
        """
        Latency-compensated actual-what-you-hear position in seconds.

        :type: float

        See also
        --------
        Project.buffer_position
            Position of next audio block being processed.
        """
        return RPR.GetPlayPositionEx(self.id)  #type:ignore

    @property
    def play_rate(self) -> float:
        """
        Project play rate at the cursor position.

        :type: float

        See also
        --------
        Project.get_play_rate
            Return project play rate at a specified time.
        """
        play_rate = RPR.Master_GetPlayRate(self.id)  #type:ignore
        return cast(float, play_rate)

    @reapy_boost.inside_reaper()
    def record(self) -> None:
        """Hit record button."""
        with self.make_current_project():
            reapy_boost.perform_action(1013)

    def redo(self) -> None:
        """
        Redo last action.

        Raises
        ------
        RedoError
            If impossible to redo.
        """
        success = RPR.Undo_DoRedo2(self.id)  #type:ignore
        if not success:
            raise RedoError

    @property
    def regions(self) -> List['reapy_boost.Region']:
        """
        List of project regions.

        :type: list of reapy_boost.Region
        """
        return self._regions_inside()

    @reapy_boost.inside_reaper()
    def _regions_inside(self) -> List['reapy_boost.Region']:
        ids = [
            RPR.EnumProjectMarkers2(  # type:ignore
                self.id, i, 0, 0, 0, 0, 0
            ) for i in range(self.n_regions + self.n_markers)
        ]
        return [
            reapy_boost.Region(self, index=i[7], enum_index=i[0] - 1)
            for i in ids if i[3]
        ]

    def save(self, force_save_as: bool = False) -> None:
        """
        Save project.

        Parameters
        ----------
        force_save_as : bool
            Force using "Save as" instead of "Save".
        """
        RPR.Main_SaveProject(self.id, force_save_as)  # type:ignore

    def select(
        self,
        start: float,
        end: Optional[float] = None,
        length: Optional[float] = None
    ) -> None:
        if end is None:
            message = "Either `end` or `length` must be specified."
            assert length is not None, message
            end = start + length
        self.time_selection = start, end

    def select_all_items(self, selected: bool = True) -> None:
        """
        Select or unselect all items, depending on `selected`.

        Parameters
        ----------
        selected : bool
            Whether to select or unselect items.
        """
        RPR.SelectAllMediaItems(self.id, selected)  # type:ignore

    def select_all_tracks(self) -> None:
        """Select all tracks."""
        self.perform_action(40296)

    @property
    def selected_envelope(self) -> Optional['reapy_boost.Envelope']:
        """
        Project selected envelope.

        :type: reapy_boost.Envelope or None
        """
        return self._selected_envelope_inside()

    @reapy_boost.inside_reaper()
    def _selected_envelope_inside(self) -> Optional['reapy_boost.Envelope']:
        selected_track = self.get_selected_track(0)
        envelope_id = cast(
            str,
            RPR.GetSelectedTrackEnvelope(self.id)  # type:ignore
        )
        envelope = None if envelope_id == 0 else reapy_boost.Envelope(
            selected_track, envelope_id
        )
        return envelope

    @property
    def selected_items(self) -> List['reapy_boost.Item']:
        """
        List of all selected items.

        :type: list of Item

        See also
        --------
        Project.get_selected_item
            Return a specific selected item.
        """
        return self._selected_items_inside()

    @reapy_boost.inside_reaper()
    def _selected_items_inside(self) -> List['reapy_boost.Item']:
        return [
            reapy_boost.Item(
                RPR.GetSelectedMediaItem(  # type:ignore
                    self.id, i
                )
            ) for i in range(self.n_selected_items)
        ]

    @property
    def selected_tracks(self) -> List['reapy_boost.Track']:
        """
        List of selected tracks (excluding master).

        :type: list of Track
        """
        return self._selected_tracks_inside()

    @selected_tracks.setter
    def selected_tracks(self, tracks: List['reapy_boost.Track']) -> None:
        self.unselect_all_tracks()
        for track in tracks:
            track.select()

    @reapy_boost.inside_reaper()
    def _selected_tracks_inside(self) -> List['reapy_boost.Track']:
        return [
            reapy_boost.Track(
                RPR.GetSelectedTrack(  # type:ignore
                    self.id, i
                )
            ) for i in range(self.n_selected_tracks)
        ]

    def set_info_string(self, param_name: str, param_string: str) -> None:
        """
        Parameters
        ----------
        param_name : str
            MARKER_GUID:X : get the GUID (unique ID) of the marker or region
                with index X, where X is the index passed to
                EnumProjectMarkers, not necessarily the displayed number
            RECORD_PATH :
                recording directory -- may be blank or a relative path,
                to get the effective path see GetProjectPathEx()
            RENDER_FILE : render directory
            RENDER_PATTERN : render file name (may contain wildcards)
            RENDER_FORMAT : base64-encoded sink configuration
                (see project files, etc). Callers can also pass a simple
                4-byte string (non-base64-encoded), e.g. "evaw" or "l3pm",
                to use default settings for that sink type.
            RENDER_FORMAT2 : base64-encoded secondary sink configuration.
                Callers can also pass a simple 4-byte string (non-base64-encoded),
                e.g. "evaw" or "l3pm", to use default settings for
                that sink type, or "" to disable secondary render.
                Formats available on this machine:
                "wave" "aiff" "iso " "ddp " "flac" "mp3l" "oggv" "OggS"
                "FFMP" "GIF " "LCF " "wvpk"
        param_string : str
        """
        RPR.GetSetProjectInfo_String(  # type:ignore
            self.id, param_name, param_string, True)

    def set_info_value(self, param_name: str, param_value: float) -> None:
        """
        Parameters
        ----------
        param_name : str
            RENDER_SETTINGS : &(1|2)=0:master mix, &1=stems+master mix,
                &2=stems only, &4=multichannel tracks to multichannel files,
                &8=use render matrix, &16=tracks with only mono media
                to mono files, &32=selected media items,
                &64=selected media items via master
            RENDER_BOUNDSFLAG : 0=custom time bounds, 1=entire project,
                2=time selection, 3=all project regions,
                4=selected media items, 5=selected project regions
            RENDER_CHANNELS : number of channels in rendered file
            RENDER_SRATE : sample rate of rendered file
                (or 0 for project sample rate)
            RENDER_STARTPOS : render start time when RENDER_BOUNDSFLAG=0
            RENDER_ENDPOS : render end time when RENDER_BOUNDSFLAG=0
            RENDER_TAILFLAG : apply render tail setting when rendering:
                &1=custom time bounds, &2=entire project, &4=time selection,
                &8=all project regions, &16=selected media items,
                &32=selected project regions
            RENDER_TAILMS : tail length in ms to render
                (only used if RENDER_BOUNDSFLAG and RENDER_TAILFLAG are set)
            RENDER_ADDTOPROJ : 1=add rendered files to project
            RENDER_DITHER : &1=dither, &2=noise shaping, &4=dither stems,
                &8=noise shaping on stems
            PROJECT_SRATE : samplerate (ignored unless PROJECT_SRATE_USE set)
            PROJECT_SRATE_USE : set to 1 if project samplerate is used
        param_value : float
        """
        RPR.GetSetProjectInfo(  # type:ignore
            self.id, param_name, param_value, True)

    def set_ext_state(
        self,
        section: str,
        key: str,
        value: Union[str, object],
        pickled: bool = False
    ) -> None:
        """
        Set external state of project.

        Parameters
        ----------
        section : str
        key : str
        value : Union[Any, str]
            State value. Will be dumped to str using either `pickle` if
            `pickled` is `True` or `json`. Length of the dumped value
            must not be over 2**31 - 2.
        pickled : bool, optional
            Data will be pickled with the last version if True.
            If you using mypy as type checker, typing_extensions.Literal[True]
            has to be used for `pickled`.

        Raises
        ------
        ValueError
            If dumped `value` has length over 2**31 - 2.
        """
        if pickled:
            value = pickle.dumps(value)
            value = codecs.encode(value, "base64").decode()
        if not isinstance(value, (str, bytes)):
            raise TypeError(
                "value has to be of type 'str', or should be picked"
            )
        if len(value) > 2**31 - 2:
            message = (
                "Dumped value length is {:,d}. It must not be over "
                "2**31 - 2."
            )
            raise ValueError(message.format(len(value)))
        RPR.SetProjExtState(self.id, section, key, value)  # type:ignore

    @reapy_boost.inside_reaper()
    def solo_all_tracks(self) -> None:
        """
        Solo all tracks in project.

        See also
        --------
        Project.unsolo_all_tracks
        """
        with self.make_current_project():
            RPR.SoloAllTracks(1)  # type:ignore

    def stop(self) -> None:
        """
        Hit stop button.
        """
        RPR.OnStopButtonEx(self.id)  # type:ignore

    @property
    def time_selection(self) -> 'reapy_boost.TimeSelection':
        """
        Project time selection.

        time_selection : reapy_boost.TimeSelection

        Can be set and deleted as follows:

        >>> project = reapy_boost.Project()
        >>> project.time_selection = 3, 8  # seconds
        >>> del project.time_selection
        """
        return self._time_selection_inside()

    @time_selection.setter
    def time_selection(self, selection: Tuple[float, float]) -> None:
        """
        Set time selection bounds.

        Parameters
        ----------
        selection : (float, float)
            Start and end of new time selection in seconds.
        """
        self.time_selection._set_start_end(*selection)

    @time_selection.deleter
    def time_selection(self) -> None:
        """
        Delete current time selection.
        """
        self.time_selection._set_start_end(0, 0)

    @reapy_boost.inside_reaper()
    def _time_selection_inside(self) -> 'reapy_boost.TimeSelection':
        time_selection = reapy_boost.TimeSelection(self)
        return time_selection

    @property
    def time_signature(self) -> Tuple[float, int]:
        """
        Project time signature.

        This does not reflect tempo envelopes but is purely what is set in the
        project settings.

        bpm : float
            Project BPM (beats per minute)
        bpi : int
            Project BPI (numerator of time signature)
        """
        _, bpm, bpi = RPR.GetProjectTimeSignature2(  # type:ignore
            self.id, 0, 0)
        return bpm, int(bpi)

    def time_signature_at_position(
        self, time: float
    ) -> Tuple[float, Tuple[int, int]]:
        """Tempo and time signature at the time.time_selection

        Parameters
        ----------
        time : float
            in seconds

        Returns
        -------
        Tuple[float, Tuple[int,int]]
            tempo (bpm): float
            numerator, denomimator Tuple[int,int]
        """
        (_, _, num, denom,
         tempo) = RPR.TimeMap_GetTimeSigAtTime(  # type:ignore
         self.id, time, 0, 0, 0)
        return tempo, (int(num), int(denom))

    def time_to_beats(self, time: float) -> float:
        """
        Convert time in seconds to beats.

        Parameters
        ----------
        time : float
            Time in seconds.

        Returns
        -------
        beats : float
            Time in beats.

        See also
        --------
        Projecr.beats_to_time
        """
        beats = RPR.TimeMap2_timeToQN(self.id, time)  # type:ignore
        return cast(float, beats)

    @property
    def tracks(self) -> 'reapy_boost.TrackList':
        """
        List of project tracks.

        :type: TrackList
        """
        return reapy_boost.TrackList(self)

    def undo(self) -> None:
        """
        Undo last action.

        Raises
        ------
        UndoError
            If impossible to undo.
        """
        success = RPR.Undo_DoUndo2(self.id)  # type:ignore
        if not success:
            raise UndoError

    def unmute_all_tracks(self) -> None:
        """
        Unmute all tracks.
        """
        self.mute_all_tracks(mute=False)

    def unselect_all_tracks(self) -> None:
        """Unselect all tracks."""
        self.perform_action(40297)

    @reapy_boost.inside_reaper()
    def unsolo_all_tracks(self) -> None:
        """
        Unsolo all tracks in project.

        See also
        --------
        Project.solo_all_tracks
        """
        with self.make_current_project():
            RPR.SoloAllTracks(0)  # type:ignore


class _MakeCurrentProject:
    """Context manager used by Project.make_current_project."""

    def __init__(self, project: Project):
        self.current_project = self._make_current_project(project)

    @staticmethod
    @reapy_boost.inside_reaper()
    def _make_current_project(project: Project) -> Project:
        """Set current project and return the previous current project."""
        current_project = reapy_boost.Project()
        RPR.SelectProjectInstance(project.id)  #type:ignore
        return current_project

    def __enter__(self) -> None:
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):  #type:ignore
        # Test for valid ID in case project has been closed since __enter__
        if self.current_project.has_valid_id:
            self.current_project.make_current_project()
