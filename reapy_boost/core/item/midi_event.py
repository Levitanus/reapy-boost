import struct
import typing as ty
from enum import IntFlag, IntEnum
import typing_extensions as te

import reapy_boost
import reapy_boost.reascript_api as RPR
from reapy_boost.core import ReapyObject, ReapyObjectList

T1 = ty.TypeVar('T1', bound='MIDIEvent')


class CCShapeFlag(IntFlag):
    square = 0
    linear = 16
    slow_start_end = 32
    fast_start = 16 | 32
    fast_end = 64
    beizer = 16 | 64

    @classmethod
    def from_shape(cls, shape: 'CCShape') -> 'CCShapeFlag':
        """
        Get flags from int enum.

        Parameters
        ----------
        shape : CCShape
            or just int from 0 to 5

        Returns
        -------
        CCShapeFlag
        """
        if shape == CCShape.square.value:
            return cls.square
        if shape == CCShape.linear.value:
            return cls.linear
        if shape == CCShape.slow_start_end.value:
            return cls.slow_start_end
        if shape == CCShape.fast_start.value:
            return cls.fast_start
        if shape == CCShape.fast_end.value:
            return cls.fast_end
        if shape == CCShape.beizer.value:
            return cls.beizer
        raise ValueError(f"Can't return flag for {shape}")


class CCShape(IntEnum):
    square = 0
    linear = 1
    slow_start_end = 2
    fast_start = 3
    fast_end = 4
    beizer = 5

    @classmethod
    def from_flag(cls, flag: CCShapeFlag) -> 'CCShape':
        """
        Get IntEnum from IntFlag.

        Parameters
        ----------
        flag : CCShapeFlag

        Returns
        -------
        CCShape
        """
        if flag == CCShapeFlag.square.value:
            return cls.square
        if flag == CCShapeFlag.linear.value:
            return cls.linear
        if flag == CCShapeFlag.slow_start_end.value:
            return cls.slow_start_end
        if flag == CCShapeFlag.fast_start.value:
            return cls.fast_start
        if flag == CCShapeFlag.fast_end.value:
            return cls.fast_end
        if flag == CCShapeFlag.beizer.value:
            return cls.beizer
        raise ValueError(f"Can't return shape for {flag}")


class MIDIEventDict(te.TypedDict):
    """
    Dict, represents trsferable midi event.

    Members
    -------
    ppq: float
    selected: bool
    muted: bool
    cc_shape: CCShapeFlag
    buf: ty.List[int]
    """

    ppq: float
    selected: bool
    muted: bool
    cc_shape: CCShapeFlag
    buf: ty.List[int]


class MIDIEventInfo(te.TypedDict):
    selected: bool
    muted: bool
    position: float
    raw_message: ty.List[int]
    ppq_position: float


class MIDIEvent(ReapyObject):
    """Abstract class for MIDI events."""

    _del_func_name = 'MIDI_DeleteEvt'
    index: int
    parent: 'reapy_boost.Take'

    def __init__(self, parent: 'reapy_boost.Take', index: int) -> None:
        """
        Create event.

        Parameters
        ----------
        parent : Take
            Take to which the event belongs.
        index : int
            Event index. It is specific to the event type, which means
            a Note and a CC can have the same index.
        """
        self.index = index
        self.parent = parent

    @property
    def _args(self) -> ty.Tuple['reapy_boost.Take', int]:
        return self.parent, self.index

    @property
    def as_dict(self) -> ty.Tuple[MIDIEventDict, ...]:
        """
        Representation of event in a dict.

        Notes
        -----
        ⋅ Can be used for inserting along with event buffer.
        ⋅ For notes and CC with beizer curve returns list of 2 items.

        :type: Tuple[MIDIEventDict]
        """
        infos = self.infos
        return (
            MIDIEventDict(
                ppq=infos['ppq_position'],
                selected=bool(infos['selected']),
                muted=bool(infos['muted']),
                cc_shape=CCShapeFlag(0),
                buf=infos['raw_message'],
            ),
        )

    def delete(self) -> None:
        """Delete event from the take."""
        f = getattr(RPR, self._del_func_name)
        f(self.parent.id, self.index)

    @property
    def infos(self) -> MIDIEventInfo:
        """
        Event info as dict.

        :type: MIDIEventInfo
            {'selected': bool,
            'muted': bool,
            'position': float,
            'message': List[int],
            'ppq_position': int}
        """
        take = self.parent
        max_eventbuf_length = 65000
        _, _, _, selected, muted, ppqpos, msg, _ = RPR.MIDI_GetEvt(
            take.id, self.index, 0, 0, 0.0, '', max_eventbuf_length
        )
        return MIDIEventInfo(
            selected=bool(selected),
            muted=bool(muted),
            position=take.ppq_to_time((ppqpos)),
            raw_message=[s for s in msg.encode('latin-1')],
            ppq_position=ppqpos
        )

    @reapy_boost.inside_reaper()
    def set(
        self,
        selected: ty.Optional[bool] = None,
        muted: ty.Optional[bool] = None,
        position: ty.Optional[float] = None,
        sort: ty.Optional[bool] = True,
        raw_message: ty.Optional[ty.List[int]] = None,
        *,
        time_unit: str = "seconds"
    ) -> None:
        """
        Set properties of event if needed.

        Note
        ----
        Optional arguments can be None, therefore will not be applied at all.

        Parameters
        ----------
        selected : bool, optional
            Whether to select new note (default=False).
        muted : bool, optional
            Whether to mute new note (default=False).
        position : float, optional
            position at take
        sort : bool, optional
            Whether to resort notes after creating new note
            (default=True). If False, then the new note will be
            ``take.notes[-1]``. Otherwise it will be at its place in
            the time-sorted list ``take.notes``. Set to False for
            improved efficiency when adding several notes, then call
            ``Take.sort_events`` at the end.
        raw_message : List[int], optional
            can be applied to every type of event, which leads to
            ignoring of the event-specific arguments.
        time_unit : str ("seconds as default")
            "beats"|"ppq"|"seconds" (default are seconds)
        """
        take = self.parent
        if position:
            position = take._resolve_midi_unit((position, ), time_unit)[0]
        if raw_message:
            raw_message = take._midi_to_bytestr(raw_message)
        RPR.MIDI_SetEvt(
            take.id, self.index, selected, muted, position, raw_message,
            len(raw_message), not sort
        )


class MIDIEventList(ReapyObjectList, ty.Generic[T1]):
    parent: 'reapy_boost.Take'

    def __init__(self, parent: 'reapy_boost.Take') -> None:
        """
        Create event list.

        Parameters
        ----------
        parent : Take
            Take to which the event list belongs.
        """
        self.parent = parent

    def __getitem__(self, key: int) -> T1:
        with reapy_boost.inside_reaper():
            if key >= len(self):
                raise IndexError
            return self._elements_class(self.parent, key)
        raise RuntimeError()

    def __len__(self) -> int:
        return ty.cast(int, getattr(self.parent, self._n_elements))

    def __iter__(self) -> ty.Iterator[T1]:
        for i in range(len(self)):
            yield self[i]

    @property
    def _args(self) -> ty.Tuple['reapy_boost.Take']:
        return self.parent,

    @property
    def _elements_class(self) -> ty.Type[T1]:
        return MIDIEvent

    @property
    def _n_elements(self) -> str:
        return 'n_midi_events'


class CCInfo(MIDIEventInfo):
    channel_message: int
    channel: int
    messages: ty.Tuple[int, int]


class CC(MIDIEvent):
    """MIDI CC event."""

    _del_func_name = 'MIDI_DeleteCC'

    @property
    def as_dict(self) -> ty.Tuple[MIDIEventDict, ...]:
        """
        Representation of event in a dict.

        Notes
        -----
        ⋅ Can be used for inserting along with event buffer.
        ⋅ For notes and CC with beizer curve returns list of 2 items.

        :type: Tuple[MIDIEventDict]
        """
        infos = self.infos
        shape = self.shape
        evt1 = MIDIEventDict(
            ppq=infos['ppq_position'],
            selected=bool(infos['selected']),
            muted=bool(infos['muted']),
            cc_shape=CCShapeFlag.from_shape(shape[0]),
            buf=infos['raw_message'],
        )
        if shape[0] == CCShape.beizer:
            evt2 = MIDIEventDict(
                ppq=infos['ppq_position'],
                selected=bool(infos['selected']),
                muted=bool(infos['muted']),
                cc_shape=CCShapeFlag.linear,
                buf=list(b'\xff\x0fCCBZ\x00' + struct.pack('<f', shape[1])),
            )
            return evt1, evt2
        return (evt1, )

    @property
    def channel(self) -> int:
        """
        CC channel between 0 and 15.

        :type: int

        See also
        --------
        CC.infos
            For maximum efficiency when querying several properties of
            a CC.
        """
        return self.infos['channel']

    @channel.setter
    def channel(self, channel: int) -> None:
        self.set(channel=channel)

    @property
    def channel_message(self) -> int:
        """
        CC channel message.

        :type: int

        See also
        --------
        CC.infos
            For maximum efficiency when querying several properties of
            a CC.
        """
        return self.infos['channel_message']

    @channel_message.setter
    def channel_message(self, channel_message: int) -> None:
        self.set(channel_message=channel_message)

    @reapy_boost.inside_reaper()
    @property
    def infos(self) -> CCInfo:
        """
        Return infos about CC.

        :type: CCInfo
            selected: bool
            muted: bool
            position: float
            ppq_position: float
            raw_message: List[int]
            channel_message: int
            channel: int
            messages: Tuple[int, int]
        """
        take = self.parent
        res = list(RPR.MIDI_GetCC(take.id, self.index, 0, 0, 0, 0, 0, 0,
                                  0))[3:]
        return CCInfo(
            selected=bool(res[0]),
            muted=bool(res[1]),
            position=take.ppq_to_time(res[2]),
            ppq_position=res[2],
            raw_message=list(int(b) for b in (res[3], *res[5:7])),
            channel_message=int(res[3]),
            channel=int(res[4]),
            messages=(int(res[5]), int(res[6])),
        )

    @property
    def messages(self) -> ty.Tuple[int, int]:
        """
        CC messages.

        :type: 2-list of int

        See also
        --------
        CC.infos
            For maximum efficiency when querying several properties of
            a CC.
        """
        return self.infos['messages']

    @messages.setter
    def messages(self, messages: ty.Tuple[int, int]) -> None:
        self.set(messages=messages)

    @property
    def muted(self) -> bool:
        """
        Whether CC is muted.

        :type: bool

        See also
        --------
        CC.infos
            For maximum efficiency when querying several properties of
            a CC.
        """
        return self.infos['muted']

    @muted.setter
    def muted(self, muted: bool) -> None:
        self.set(muted=muted)

    @property
    def position(self) -> float:
        """
        CC position in seconds.

        :type: float

        See also
        --------
        CC.infos
            For maximum efficiency when querying several properties of
            a CC.
        """
        return self.infos["position"]

    @position.setter
    def position(self, position: float) -> None:
        self.set(position=position)

    @property
    def selected(self) -> bool:
        """
        Whether CC is selected.

        :type: bool

        See also
        --------
        CC.infos
            For maximum efficiency when querying several properties of
            a CC.
        """
        return self.infos['selected']

    @selected.setter
    def selected(self, selected: bool) -> None:
        self.set(selected=selected)

    @reapy_boost.inside_reaper()
    def set(
        self,
        selected: ty.Optional[bool] = None,
        muted: ty.Optional[bool] = None,
        position: ty.Optional[float] = None,
        sort: ty.Optional[bool] = True,
        raw_message: ty.Optional[ty.List[int]] = None,
        channel_message: ty.Optional[int] = None,
        channel: ty.Optional[int] = None,
        messages: ty.Optional[ty.List[int]] = None,
        *,
        time_unit: str = "seconds"
    ) -> None:
        """
        Set properties of event if needed.

        Note
        ----
        Optional arguments can be None, therefore will not be applied at all.

        Parameters
        ----------
        selected : bool, optional
            Whether to select new note (default=False).
        muted : bool, optional
            Whether to mute new note (default=False).
        position : float, optional
            position at take
        sort : bool, optional
            Whether to resort notes after creating new note
            (default=True). If False, then the new note will be
            ``take.notes[-1]``. Otherwise it will be at its place in
            the time-sorted list ``take.notes``. Set to False for
            improved efficiency when adding several notes, then call
            ``Take.sort_events`` at the end.
        raw_message : List[int], optional
            can be applied to every type of event, which leads to
            ignoring of the event-specific arguments.
        channel_message : int, optional
            0xb0 for example
        channel : int, optional
        messages : Tuple[int, int], optional
            CC_num, value
        time_unit : str Optional
            "beats"|"ppq"|"seconds" (default are seconds)
        """
        take = self.parent
        if position:
            position = take._resolve_midi_unit((position, ), time_unit)[0]
        if sort is not None:
            sort = not sort
        if messages and not raw_message:
            msg2, msg3 = messages
        if raw_message:
            channel_message, msg2, msg3 = raw_message
            channel = None
        RPR.MIDI_SetCC(
            take.id, self.index, selected, muted, position, channel_message,
            channel, msg2, msg3, sort
        )

    @property
    def shape(self) -> ty.Tuple[CCShape, float]:
        """
        Shape type and beizer tension.

        :type: Tuple[CCShape, float]
            shape can be passed as enum instance or as int
        """
        _, _, _, shape_i, tension = RPR.MIDI_GetCCShape(
            self.parent.id, self.index, 1, 0.1
        )
        return CCShape(shape_i), tension

    @shape.setter
    def shape(self, shape: CCShape) -> None:
        shape_i = CCShape(shape[0]).value
        tension = shape[1]
        RPR.MIDI_SetCCShape(self.parent.id, self.index, shape_i, tension, None)


class CCList(MIDIEventList[CC]):

    _elements_class = CC
    _n_elements = "n_cc"


class NoteInfo(MIDIEventInfo):
    end: float
    ppq_end: float
    channel: int
    pitch: int
    velocity: int


class Note(MIDIEvent):
    """MIDI note."""

    _del_func_name = 'MIDI_DeleteNote'

    @property
    def as_dict(self) -> ty.Tuple[MIDIEventDict, MIDIEventDict]:
        """
        Representation of event in a dict.

        Notes
        -----
        ⋅ Can be used for inserting along with event buffer.
        ⋅ For notes and CC with beizer curve returns list of 2 items.

        :type: Tuple[MIDIEventDict, MIDIEventDict]
            note on and note off
        """
        infos = self.infos
        off = [infos['raw_message'][0] - 0x10, *infos['raw_message'][1:3]]
        return (
            MIDIEventDict(
                ppq=infos['ppq_position'],
                selected=bool(infos['selected']),
                muted=bool(infos['muted']),
                cc_shape=CCShapeFlag(0),
                buf=infos['raw_message'],
            ),
            MIDIEventDict(
                ppq=infos['ppq_end'],
                selected=bool(infos['selected']),
                muted=bool(infos['muted']),
                cc_shape=CCShapeFlag(0),
                buf=off,
            )
        )

    @property
    def channel(self) -> int:
        """
        Note channel between 0 and 15.

        :type: int

        See also
        --------
        Note.infos
            For maximum efficiency when querying several properties of
            a Note.
        """
        return self.infos['channel']

    @channel.setter
    def channel(self, channel: int) -> None:
        self.set(channel=channel)

    @property
    def end(self) -> float:
        """
        Note end in seconds.

        :type: float

        See also
        --------
        Note.infos
            For maximum efficiency when querying several properties of
            a Note.
        """
        return self.infos["end"]

    @end.setter
    def end(self, end: float) -> None:
        self.set(end=end)

    @property
    def infos(self) -> NoteInfo:
        """
        Return infos about note.

        :type: NoteInfo
            selected: bool
            muted: bool
            position: float
            ppq_position: float
            raw_message: [0x9+ch, note, vel]
            end: float
            ppq_end: float
            channel: int
            pitch: int
            velocity: int
        """
        take = self.parent
        res = list(RPR.MIDI_GetNote(take.id, self.index, 0, 0, 0, 0, 0, 0,
                                    0))[3:]
        ch, note, vel = int(res[4]), int(res[5]), int(res[6])
        return NoteInfo(
            selected=bool(res[0]),
            muted=bool(res[1]),
            position=take.ppq_to_time(res[2]),
            ppq_position=res[2],
            raw_message=[0x90 + ch, note, vel],
            end=take.ppq_to_time(res[3]),
            ppq_end=res[3],
            channel=ch,
            pitch=note,
            velocity=vel
        )

    @property
    def muted(self) -> bool:
        """
        Whether note is muted.

        :type: bool

        See also
        --------
        Note.infos
            For maximum efficiency when querying several properties of
            a Note.
        """
        return self.infos['muted']

    @muted.setter
    def muted(self, muted: bool) -> None:
        self.set(muted=muted)

    @property
    def pitch(self) -> int:
        """
        Note pitch between 0 and 127.

        :type: int

        See also
        --------
        Note.infos
            For maximum efficiency when querying several properties of
            a Note.
        """
        return self.infos['pitch']

    @pitch.setter
    def pitch(self, pitch: int) -> None:
        self.set(pitch=pitch)

    @property
    def selected(self) -> bool:
        """
        Whether note is selected.

        :type: bool

        See also
        --------
        Note.infos
            For maximum efficiency when querying several properties of
            a Note.
        """
        return self.infos['selected']

    @selected.setter
    def selected(self, selected: bool) -> None:
        self.set(selected=selected)

    @reapy_boost.inside_reaper()
    def set(
        self,
        selected: ty.Optional[bool] = None,
        muted: ty.Optional[bool] = None,
        position: ty.Optional[float] = None,
        sort: ty.Optional[bool] = True,
        raw_message: ty.Optional[ty.List[int]] = None,
        end: ty.Optional[float] = None,
        channel: ty.Optional[int] = None,
        pitch: ty.Optional[int] = None,
        velocity: ty.Optional[int] = None,
        *,
        time_unit: str = "seconds"
    ) -> None:
        """
        Set properties of event if needed.

        Note
        ----
        Optional arguments can be None, thereforce will not be applied at all.

        Parameters
        ----------
        selected : bool, optional
            Whether to select new note (default=False).
        muted : bool, optional
            Whether to mute new note (default=False).
        position : float, optional
            position at take
        sort : bool, optional
            Whether to resort notes after creating new note
            (default=True). If False, then the new note will be
            ``take.notes[-1]``. Otherwise it will be at its place in
            the time-sorted list ``take.notes``. Set to False for
            improved efficiency when adding several notes, then call
            ``Take.sort_events`` at the end.
        raw_message : List[int], optional
            can be applied to every type of event, which leads to
            ignoring of the event-specific arguments.
        end : float
        channel : int
        pitch : int
        velocity : int
        time_unit : str ("seconds as default")
            "beats"|"ppq"|"seconds" (default are seconds)
        """
        take = self.parent
        if position:
            position = take._resolve_midi_unit((position, ), time_unit)[0]
        if end:
            end = take._resolve_midi_unit((end, ), time_unit)[0]
        if raw_message:
            rm = raw_message
            channel, pitch, velocity = rm[0] % 0x90, rm[1], rm[2]
        if sort is not None:
            sort = not sort
        RPR.MIDI_SetNote(
            take.id, self.index, selected, muted, position, end, channel,
            pitch, velocity, sort
        )

    @property
    def start(self) -> float:
        """
        Note start in seconds.

        :type: float

        See also
        --------
        Note.infos
            For maximum efficiency when querying several properties of
            a Note.
        """
        return self.infos["position"]

    @start.setter
    def start(self, start: float) -> None:
        self.set(position=start)

    @property
    def velocity(self) -> int:
        """
        Note velocity between 0 and 127.

        :type: int

        See also
        --------
        Note.infos
            For maximum efficiency when querying several properties of
            a Note.
        """
        return self.infos['velocity']

    @velocity.setter
    def velocity(self, velocity: int) -> None:
        self.set(velocity=velocity)


class NoteList(MIDIEventList[Note]):

    _elements_class = Note
    _n_elements = "n_notes"


class TextSysexInfo(MIDIEventInfo):
    type_: int


class TextSysex(MIDIEvent):
    """Abstract class for Text or Sysex events."""

    _del_func_name = 'MIDI_DeleteTextSysexEvt'

    @property
    def infos(self) -> TextSysexInfo:
        """
        Event info as dict.

        :type: TextSysexInfo
            {'selected': bool,
            'muted': bool,
            'position': float,
            'message': List[int],
            'ppq_position': float,
            'type_': int
            }
        """
        take = self.parent
        max_eventbuf_length = 65000
        _, _, _, sel, muted, ppqpos, type_, msg, _ = RPR.MIDI_GetTextSysexEvt(
            take.id, self.index, 0, 0, 0.0, 0, '', max_eventbuf_length
        )
        return TextSysexInfo(
            selected=bool(sel),
            muted=bool(muted),
            position=take.ppq_to_time((ppqpos)),
            raw_message=[s for s in msg.encode('latin-1')],
            ppq_position=ppqpos,
            type_=int(type_)
        )

    @reapy_boost.inside_reaper()
    def set(
        self,
        selected: ty.Optional[bool] = None,
        muted: ty.Optional[bool] = None,
        position: ty.Optional[float] = None,
        sort: ty.Optional[bool] = True,
        raw_message: ty.Optional[ty.List[int]] = None,
        type_: ty.Optional[int] = None,
        *,
        time_unit: str = "seconds"
    ) -> None:
        """
        Set properties of event if needed.

        Notes
        -----
        ⋅ Optional arguments can be None, therefore will not be applied at all
        ⋅ type_ is NOT optional when new raw_message is assigned

        Parameters
        ----------
        selected : bool, optional
            Whether to select new note (default=False).
        muted : bool, optional
            Whether to mute new note (default=False).
        position : float, optional
            position at take
        sort : bool, optional
            Whether to resort notes after creating new note
            (default=True). If False, then the new note will be
            ``take.notes[-1]``. Otherwise it will be at its place in
            the time-sorted list ``take.notes``. Set to False for
            improved efficiency when adding several notes, then call
            ``Take.sort_events`` at the end.
        raw_message : List[int], optional
            can be applied to every type of event, which leads to
            ignoring of the event-specific arguments.
        type_ : int, optional
            -1:sysex (msg should not include bounding F0..F7),
            1-14:MIDI text event types,
            15=REAPER notation event.
        time_unit : str ("seconds as default")
            "beats"|"ppq"|"seconds" (default are seconds)
        """
        take = self.parent
        print('called')
        if position:
            position = take._resolve_midi_unit((position, ), time_unit)[0]
        if raw_message:
            raw_message = take._midi_to_bytestr(raw_message)
            print(raw_message, len(raw_message))
        RPR.MIDI_SetTextSysexEvt(
            take.id, self.index, selected, muted, position, type_, raw_message,
            len(raw_message), not sort
        )

    @property
    def type_(self) -> int:
        """
        Meta event type

        :type: int
            -1:sysex (msg should not include bounding F0..F7),
            1-14:MIDI text event types,
            15=REAPER notation event.
        """
        return self.infos['type_']

    @type_.setter
    def type_(self, type_: int) -> None:
        self.set(type_=type_)


class TextSysexList(MIDIEventList[TextSysex]):

    _elements_class = TextSysex
    _n_elements = "n_text_sysex"
