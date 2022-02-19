import struct
from typing import Iterable, List, Optional, Tuple, Union, cast
import reapy_boost
from reapy_boost import reascript_api as RPR
from reapy_boost.core import ReapyObject


class Take(ReapyObject):

    _class_name = "Take"

    def __init__(self, id: str):
        self.id = id

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Take) and self.id == other.id

    @property
    def _args(self) -> Tuple[str]:
        return self.id,

    def add_audio_accessor(self) -> 'reapy_boost.AudioAccessor':
        """
        Create audio accessor and return it.

        Returns
        -------
        audio_accessor : AudioAccessor
            Audio accessor on take.
        """
        audio_accessor_id = RPR.CreateTakeAudioAccessor(self.id)  # type:ignore
        audio_accessor = reapy_boost.AudioAccessor(audio_accessor_id)
        return audio_accessor

    @reapy_boost.inside_reaper()
    def add_event(
        self,
        message: Iterable[int],
        position: float,
        unit: str = "seconds"
    ) -> None:
        """
        Add generic event to the take at position.

        Note
        ----
        ⋅ No sort events during this call
        ⋅ Inserting notes within this function causes problems
            (wrong note on and off timing), this is known REAPER bug.
            Use `Take.add_note` instead.

        Parameters
        ----------
        message : Iterable[int]
            Can be any message buffer, for example: (0xb0, 64, 127)
            which is CC64 val127 on channel 1
        position : float
            position at take
        unit : str, optional
            "beats"|"ppq"|"seconds" (default are seconds)

        See also
        --------
        Take.add_note
        """
        ppqpos = self._resolve_midi_unit((position, ), unit)[0]
        bytestr = self._midi_to_bytestr(message)
        RPR.MIDI_InsertEvt(  # type:ignore
            self.id, False, False, ppqpos, bytestr, len(bytestr)
        )

    def add_fx(
        self, name: str, even_if_exists: bool = True
    ) -> 'reapy_boost.FX':
        """
        Add FX to track and return it.

        Parameters
        ----------
        name : str
            FX name.
        even_if_exists : bool, optional
            Whether the FX should be added even if there already is an
            instance of the same FX on the track (default=True).

        Returns
        -------
        fx : FX
            New FX on take (or previously existing instance of FX if
            even_if_exists=False).

        Raises
        ------
        ValueError
            If there is no FX with the specified name.
        """
        index = RPR.TakeFX_AddByName(  # type:ignore
            self.id, name, 1 - 2 * even_if_exists)
        if index == -1:
            raise ValueError("Can't find FX named {}".format(name))
        fx = reapy_boost.FX(cast('reapy_boost.Take', self), index)
        return fx

    @reapy_boost.inside_reaper()
    def add_note(
        self,
        start: float,
        end: float,
        pitch: int,
        velocity: int = 100,
        channel: int = 0,
        selected: bool = False,
        muted: bool = False,
        unit: str = "seconds",
        sort: bool = True
    ) -> None:
        """
        Add MIDI note to take.

        Parameters
        ----------
        start : float
            Note start. Unit depends on ``unit``.
        end : float
            Note end. Unit depends on ``unit``.
        pitch : int
            Note pitch between 0 and 127.
        velocity : int, optional
            Note velocity between 0 and 127 (default=100).
        channel : int, optional
            MIDI channel between 0 and 15.
        selected : bool, optional
            Whether to select new note (default=False).
        muted : bool
            Whether to mute new note (default=False).
        unit : {"seconds", "ppq", "beats"}, optional
            Time unit for ``start`` and ``end`` (default="seconds").
            ``"ppq"`` refers to MIDI ticks.
        sort : bool, optional
            Whether to resort notes after creating new note
            (default=True). If False, then the new note will be
            ``take.notes[-1]``. Otherwise it will be at its place in
            the time-sorted list ``take.notes``. Set to False for
            improved efficiency when adding several notes, then call
            ``Take.sort_events`` at the end.

        See also
        --------
        Take.sort_events
        """
        start, end = self._resolve_midi_unit((start, end), unit)
        sort = bool(not sort)
        args = (
            self.id, selected, muted, start, end, channel, pitch, velocity,
            sort
        )
        RPR.MIDI_InsertNote(*args)  # type:ignore

    @reapy_boost.inside_reaper()
    def add_sysex(
        self,
        message: Iterable[int],
        position: float,
        unit: str = "seconds",
        evt_type: int = -1
    ) -> None:
        """
        Add SysEx event to take.

        Notes
        -----
        ⋅ No sort events during this call
        ⋅ No need to add 0xf0 ... 0xf7 bytes (they will be doubled)

        Parameters
        ----------
        message : Iterable[int]
            Can be any message buffer, for example: (0xb0, 64, 127)
            which is CC64 val127 on channel 1
        position : float
            position at take
        unit : str, optional
            "beats"|"ppq"|"seconds" (default are seconds)
        evt_type: int (default -1)
            Allowable types are
            ⋅ -1:sysex (msg should not include bounding F0..F7),
            ⋅ 1-14:MIDI text event types,
            ⋅ 15=REAPER notation event.
        """
        bytestr = self._midi_to_bytestr(message)
        ppqpos = self._resolve_midi_unit((position, ), unit)[0]
        RPR.MIDI_InsertTextSysexEvt(  # type:ignore
            self.id, False, False, ppqpos, evt_type, bytestr, len(bytestr)
        )

    def beat_to_ppq(self, beat: float) -> int:
        """
        Convert beat number (from project start) to MIDI ticks (of the take).

        Parameters
        ----------
        beat : float
            Beat time to convert in beats.

        Returns
        -------
        ppq : float
            Converted time in MIDI ticks of current take.

        See also
        --------
        Take.ppq_to_beat
        Take.time_to_ppq
        """
        ppq = RPR.MIDI_GetPPQPosFromProjQN(self.id, beat)  # type:ignore
        return int(ppq)

    @property
    def cc_events(self) -> 'reapy_boost.CCList':
        """
        List of CC events on take.

        :type: CCList
        """
        return reapy_boost.CCList(cast('reapy_boost.Take', self))

    @property
    def envelopes(self) -> 'reapy_boost.EnvelopeList':
        return reapy_boost.EnvelopeList(cast('reapy_boost.Take', self))

    @property
    def fxs(self) -> 'reapy_boost.FXList':
        """
        FXs on take.

        :type: FXList
        """
        return reapy_boost.FXList(cast('reapy_boost.Take', self))

    def get_info_value(self, param_name):
        return RPR.GetMediaItemTakeInfo_Value(  # type:ignore
            self.id, param_name)

    @property
    def has_valid_id(self) -> bool:
        """
        Whether ReaScript ID is still valid.

        For instance, if take has been deleted, ID will not be valid
        anymore.

        :type: bool
        """
        return self._has_valid_id_inside()

    @reapy_boost.inside_reaper()
    def _has_valid_id_inside(self) -> bool:
        try:
            project_id = self.track.project.id
        except (OSError, AttributeError):
            return False
        pointer, name = self._get_pointer_and_name()
        return bool(RPR.ValidatePtr2(project_id, pointer, name))

    @property
    def is_active(self) -> bool:
        """
        Whether take is active.

        :type: bool
        """
        return self._is_active_inside()

    @reapy_boost.inside_reaper()
    def _is_active_inside(self) -> bool:
        return self == self.item.active_take

    @property
    def is_midi(self) -> bool:
        """
        Whether take contains MIDI or audio.

        :type: bool
        """
        return bool(RPR.TakeIsMIDI(self.id))  # type:ignore

    @property
    def item(self) -> 'reapy_boost.Item':
        """
        Parent item.

        :type: Item
        """
        return reapy_boost.Item(
            cast(
                str,
                RPR.GetMediaItemTake_Item(  # type:ignore
                    self.id
                )
            )
        )

    @reapy_boost.inside_reaper()
    def get_midi(
        self,
        size: int = 2 * 1024 * 1024
    ) -> List['reapy_boost.MIDIEventDict']:
        """
        Get all midi data of take in one call.

        Parameters
        ----------
        size : int, optional
            predicted size of event buffer to allocate.
            For performance is better to set it to something a but bigger
            than expected buffer size.
            Event with common midi-message (3-bytes) takes 12 bytes.

        Returns
        -------
        List[MIDIEventDict]
            ppq: int
            selected: bool
            muted: bool
            cc_shape: CCShapeFlag
            buf: ty.List[int]

        See also
        --------
        Take.set_midi
        """
        buf: str
        _, _, buf, _ = RPR.MIDI_GetAllEvts(  # type:ignore
            self.id, '', size
        )
        msg = buf.encode('latin-1')
        out = []
        i = 0
        ppq = 0
        length = len(msg)
        while i < length:
            if length - i < 9:
                break
            ofst, flag, len_ = (
                struct.unpack('<I', msg[i:i + 4])[0], int(msg[i + 4]),
                struct.unpack('<I', msg[i + 5:i + 9])[0]
            )
            ppq += ofst
            buf_b = msg[i + 9:i + 9 + len_]
            buf_int = [int(b) for b in buf_b]
            i += 9 + len_
            if len_ == 0:
                i += 1
                continue
            out.append(
                reapy_boost.MIDIEventDict(
                    ppq=ppq,
                    selected=bool(flag & 1),
                    muted=bool(flag & 2),
                    cc_shape=reapy_boost.CCShapeFlag(flag & 0b11110000),
                    buf=buf_int
                )
            )
        return out

    @property
    def guid(self) -> str:
        """
        Used for communication within other scripts.

        :type: str
        """
        _, _, _, guid, _ = RPR.GetSetMediaItemTakeInfo_String(  # type:ignore
            self.id, 'GUID', 'stringNeedBig', False
        )
        return guid

    def make_active_take(self) -> bool:
        """
        Make take active.
        """
        RPR.SetActiveTake(self.id)  # type:ignore

    @property
    def midi_events(self) -> 'reapy_boost.MIDIEventList':
        """
        Get all midi events as EventList.

        Returns
        -------
        MIDIEventList
        """
        return reapy_boost.MIDIEventList(cast('reapy_boost.Take', self))

    def midi_hash(self, notes_only: bool = False) -> str:
        """
        Get hash of MIDI-data to compare with later.

        Parameters
        ----------
        notes_only : bool, (False by default)
            count only notes if True

        Returns
        -------
        str
        """
        return RPR.MIDI_GetHash(  # type:ignore
            self.id, notes_only, 'hash', 1024**2)[3]

    def _midi_to_bytestr(self, message: Iterable[int]) -> str:
        return bytes(message).decode('latin-1')

    @property
    def n_cc(self) -> int:
        """
        Number of MIDI CC events in take (always 0 for audio takes).

        :type: int
        """
        return RPR.MIDI_CountEvts(self.id, 0, 0, 0)[3]  # type:ignore

    @property
    def n_envelopes(self) -> int:
        """
        Number of envelopes on take.

        :type: int
        """
        return RPR.CountTakeEnvelopes(self.id)  # type:ignore

    @property
    def n_fxs(self) -> int:
        """
        Number of FXs on take.

        :type: int
        """
        return RPR.TakeFX_GetCount(self.id)  # type:ignore

    @property
    def n_midi_events(self) -> int:
        """
        Number of MIDI events in take.

        :type: int
        """
        return RPR.MIDI_CountEvts(self.id, 1, 1, 1)[0]  # type:ignore

    @property
    def n_notes(self) -> int:
        """
        Number of MIDI notes in take (always 0 for audio takes).

        :type: int
        """
        return RPR.MIDI_CountEvts(self.id, 0, 0, 0)[2]  # type:ignore

    @property
    def n_text_sysex(self) -> int:
        """
        Number of MIDI text/sysex events in take (0 for audio takes).

        :type: int
        """
        return RPR.MIDI_CountEvts(self.id, 0, 0, 0)[4]  # type:ignore

    @property
    def name(self) -> str:
        """
        Take name.

        :type: str
        """
        if self._is_defined:
            return RPR.GetTakeName(self.id)  # type:ignore
        return ""

    @name.setter
    def name(self, name: str) -> None:
        RPR.GetSetMediaItemTakeInfo_String(  # type:ignore
            self.id, "P_NAME", name, True)

    @property
    def notes(self) -> 'reapy_boost.NoteList':
        """
        List of MIDI notes on take.

        Unless ``Take.add_note`` has been called with ``sort=False``,
        notes are time-sorted.

        :type: NoteList
        """
        return reapy_boost.NoteList(cast('reapy_boost.Take', self))

    def ppq_to_beat(self, ppq: Union[int, float]) -> float:
        """
        Convert time in MIDI ticks to beats.

        Note
        ----
        Ticks are counted from take start, beats — from project start.

        Parameters
        ----------
        ppq : float
            Time to convert in MIDI ticks.

        Returns
        -------
        beat : float
            Converted time in beats.

        See also
        --------
        Take.beat_to_ppq
        Take.ppq_to_time
        """
        beat = RPR.MIDI_GetProjQNFromPPQPos(self.id, ppq)  # type:ignore
        return beat

    def ppq_to_time(self, ppq: Union[int, float]) -> float:
        """
        Convert time in MIDI ticks to seconds.

        Parameters
        ----------
        ppq : float
            Time to convert in MIDI ticks.

        Returns
        -------
        time : float
            Converted time in seconds.

        See also
        --------
        Take.time_to_ppq
        """
        time = RPR.MIDI_GetProjTimeFromPPQPos(self.id, ppq)  # type:ignore
        return time

    @property
    def project(self) -> 'reapy_boost.Project':
        """
        Take parent project.

        :type: reapy_boost.Project
        """
        return self._project_inside()

    @reapy_boost.inside_reaper()
    def _project_inside(self) -> 'reapy_boost.Project':
        return self.item.project

    @reapy_boost.inside_reaper()
    def _resolve_midi_unit(
        self,
        pos_tuple: Tuple[float, ...],
        unit: str = "seconds"
    ) -> Tuple[float, ...]:
        """Get positions as ppq from tuple of positions of any length.

        Parameters
        ----------
        pos_tuple : Tuple[float, ...]
            tuple of position time in bets, ppq or seconds.
        unit : str, optional
            type of position inside tuple: seconds|beats|ppq

        Returns
        -------
        Tuple[float, ...]
            the same tuple normalized to ppq
        """
        if unit == "ppq":
            return pos_tuple
        # item_start_seconds = self.item.position

        def resolver(pos):
            if unit == "beats":
                return self.beat_to_ppq(pos)
            if unit == "seconds":
                return self.time_to_ppq(pos)
            raise ValueError('unit param should be one of seconds|beats|ppq')

        return cast(Tuple[int, int], (resolver(pos) for pos in pos_tuple))

    def select_all_midi_events(self, select: bool = True) -> None:
        """
        Select or unselect all MIDI events.

        Parameters
        ----------
        select : bool
            Whether to select or unselect events.

        See also
        --------
        Take.unselect_all_midi_events
        """
        RPR.MIDI_SelectAll(self.id, select)  # type:ignore

    def set_info_value(self, param_name, value):
        return RPR.SetMediaItemTakeInfo_Value(  # type:ignore
            self.id, param_name, value)

    @reapy_boost.inside_reaper()
    def set_midi(
        self,
        midi: List['reapy_boost.MIDIEventDict'],
        start: Optional[float] = None,
        unit: str = "seconds",
        sort: bool = True
    ):
        """
        Erase all midi from take and build new one from scratch.

        Parameters
        ----------
        midi : List[MIDIEventDict]
            can be taken with `Take.get_midi()` or build from scratch.
        start : float, optional
            if offset needed (for example, start from a particular time)
        unit : str, optional
            time unit: "seconds"|"beats"|"ppq"
        sort : bool, optional
            if sort is needed after insertion

        Raises
        ------
        NotImplementedError
            currently, gaps between events longer than several hours
            are not supported.

        See also
        --------
        Take.get_midi
        """
        out = b''
        start_ppq = 0
        if start is not None:
            start_ppq = self._resolve_midi_unit((start, ), unit)[0]
        last_ppq = 0 - start_ppq
        for msg in midi:
            evt = b''
            ofst_i = msg['ppq'] - last_ppq
            if ofst_i > 4294967295:
                raise NotImplementedError(
                    'ofset larger than 4294967295 currently not supported'
                )
                # something done with big offset
                # it is about many-many-many hours between events
                # (1 hour is about 8000000 ppq in 120 bpm)
            ofst = struct.pack('<I', int(ofst_i))
            evt += ofst
            last_ppq = msg['ppq']

            flag = bytes(
                [
                    int(msg['selected']) | (int(msg['muted']) << 1)
                    | msg['cc_shape']
                ]
            )
            evt += flag

            len_ = struct.pack('<I', len(msg['buf']))
            evt += len_

            buf = bytes(msg['buf'])
            evt += buf
            out += evt
        packed = out.decode('latin-1')
        RPR.MIDI_SetAllEvts(self.id, packed, len(packed))  # type:ignore
        if sort:
            self.sort_events()

    def sort_events(self) -> None:
        """
        Sort MIDI events on take.

        This is only needed if ``Take.add_note`` was called with
        ``sort=False``.

        Examples
        --------
        The following example creates 100 MIDI notes on take in
        reversed order, with ``sort=False`` for efficiency. Thus,
        ``take.notes`` is not time-sorted. ``take.sort_events`` is
        called afterwards so that ``take.notes`` is time-sorted.

        >>> for i in range(100):
        ...     take.add_note(99 - i, 100 - i, pitch=0, sort=False)
        ...
        >>> take.notes[0].start, take.notes[1].start
        99.0, 98.0
        >>> take.sort_events()
        >>> take.notes[0].start, take.notes[1].start
        0.0, 1.0
        """
        RPR.MIDI_Sort(self.id)  # type:ignore

    @property
    def source(self) -> 'reapy_boost.Source':
        """
        Take source.

        :type: Source
        """
        return reapy_boost.Source(
            cast(
                str,
                RPR.GetMediaItemTake_Source(  # type:ignore
                    self.id
                )
            )
        )

    @source.setter
    def source(self, source: 'reapy_boost.Source') -> None:
        RPR.SetMediaItemTake_Source(self.id, source.id)  # type:ignore

    @property
    def start_offset(self) -> float:
        """
        Start time of the take relative to start of source file.

        :type: float
        """
        return self.get_info_value("D_STARTOFFS")

    @start_offset.setter
    def start_offset(self, value: float) -> None:
        self.set_info_value("D_STARTOFFS", value)

    @property
    def text_sysex_events(self) -> 'reapy_boost.TextSysexList':
        """
        List of text or SysEx events.

        :type: TextSysexList
        """
        return reapy_boost.TextSysexList(cast('reapy_boost.Take', self))

    def time_to_ppq(self, time: float) -> int:
        """
        Convert time in seconds to MIDI ticks.

        Parameters
        ----------
        time : float
            Time to convert in seconds.

        Returns
        -------
        ppq : float
            Converted time in MIDI ticks.

        See also
        --------
        Take.ppq_to_time
        """
        ppq = RPR.MIDI_GetPPQPosFromProjTime(self.id, time)  # type:ignore
        return int(ppq)

    @property
    def track(self) -> 'reapy_boost.Track':
        """
        Parent track of take.

        :type: Track
        """
        track_id = RPR.GetMediaItemTake_Track(self.id)  # type:ignore
        return reapy_boost.Track(cast(str, track_id))

    def unselect_all_midi_events(self) -> None:
        """
        Unselect all MIDI events.

        See also
        --------
        Take.select_all_midi_events
        """
        self.select_all_midi_events(select=False)

    @property
    def visible_fx(self) -> Optional['reapy_boost.FX']:
        """
        Visible FX in FX chain if any, else None.

        :type: FX or NoneType
        """
        with reapy_boost.inside_reaper():
            return self.fxs[cast(
                int,
                RPR.TakeFX_GetChainVisible(  # type:ignore
                    self.id
                )
            )]
