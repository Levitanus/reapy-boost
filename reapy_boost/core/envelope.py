import typing as ty

import reapy_boost
from reapy_boost import reascript_api as RPR
from reapy_boost.core.item.take import Take
from reapy_boost.core.reapy_object import ReapyObject
from reapy_boost.core.track.automation_item import AutomationItem
from reapy_boost.core.track.track import Track


class EnvelopePoint(ty.TypedDict):
    """Dictionary represents envelope point.

    Members
    -------
    index: int
    time: float
    value: float
    shape: int
    tension: float
    selected: float
    """

    index: int
    time: float
    value: float
    shape: int
    tension: float
    selected: float


class Envelope(ReapyObject):

    def __init__(self, parent: ty.Union[Track, Take], id: str) -> None:
        self.id = id
        self._parent = parent

    @property
    def _args(self) -> ty.Tuple[ty.Union[Track, Take], str]:
        return (self.parent, self.id)

    def add_item(
        self,
        position: float = 0.,
        length: float = 1.,
        pool: int = 0
    ) -> AutomationItem:
        """
        Add automation item to envelope.

        Parameters
        ----------
        position : float, optional
            New item position in seconds (default=0).
        length : float
            New item length in seconds (default=0).
        pool : int
            New item pool index. If >= 0 the automation item will be a
            new instance of that pool (which will be created as an
            empty instance if it does not exist).

        Returns
        -------
        item : reapy_boost.AutomationItem
            New automation item.
        """
        item_index = RPR.InsertAutomationItem(  # type: ignore
            self.id,
            pool,
            position,
            length
        )
        item = reapy_boost.AutomationItem(envelope=self, index=item_index)
        return item

    def delete_points_in_range(self, start: float, end: float) -> None:
        """
        Delete envelope points between `start` and `end`.

        Parameters
        ----------
        start : float
            Range start in seconds.
        end : float
            Range end in seconds.
        """
        RPR.DeleteEnvelopePointRange(self.id, start, end)  # type:ignore

    @reapy_boost.inside_reaper()
    def get_derivatives(self,
                        time: float,
                        raw: bool = False) -> ty.Tuple[float, float, float]:
        """
        Return envelope derivatives of order 1, 2, 3 at a given time.

        Parameters
        ----------
        time : float
            Time in seconds.
        raw : bool, optional
            Whether to return raw values or the human-readable version
            which is printed in REAPER GUI (default=False).

        Returns
        -------
        d, d2, d3 : float
            First, second and third order derivatives.

        Examples
        --------
        >>> envelope = track.envelopes["Pan"]
        >>> envelope.get_derivatives(10, raw=True)
        (0.10635556358181712, 0.2127113398749741, 0.21271155258652666)
        >>> envelope.get_value(10)  # human-readable
        ('10%L', '21%L', '21%L')
        """
        d, d2, d3 = RPR.Envelope_Evaluate(  # type:ignore
            self.id,
            time,
            1,
            1,
            0,
            0,
            0,
            0
        )[6:]
        if not raw:
            d = RPR.Envelope_FormatValue(  # type:ignore
                self.id, d, "", 2048
            )[2]
            d2 = RPR.Envelope_FormatValue(  # type:ignore
                self.id,
                d2,
                "",
                2048
            )[2]
            d3 = RPR.Envelope_FormatValue(  # type:ignore
                self.id,
                d3,
                "",
                2048
            )[2]
        return d, d2, d3

    @reapy_boost.inside_reaper()
    def get_value(self,
                  time: float,
                  raw: bool = False) -> ty.Union[float, str]:
        """
        Return envelope value at a given time.

        Parameters
        ----------
        time : float
            Time in seconds.
        raw : bool, optional
            Whether to return raw value or its human-readable version,
            which is the one that is printed in REAPER GUI
            (default=False).

        Returns
        -------
        value : float or str
            Envelope value.

        Examples
        --------
        >>> envelope = track.envelopes["Pan"]
        >>> envelope.get_value(10, raw=True)
        -0.5145481809245827
        >>> envelope.get_value(10)  # human-readable
        '51%R'
        """
        value = RPR.Envelope_Evaluate(  # type:ignore
            self.id, time, 0, 0, 0, 0, 0, 0)[5]
        if not raw:
            value = RPR.Envelope_FormatValue(  # type:ignore
                self.id, value, "", 2048)[2]
        return value

    def get_point(self, index: int) -> EnvelopePoint:
        """Get EvnelopePoint as dictionary.

        Parameters
        ----------
        index : int
            point index

        Returns
        -------
        EnvelopePoint
        """
        (_, _, index, time, value, shape, tension,
         selected) = RPR.GetEnvelopePoint(  # type:ignore
             self.id,
             index,
             0.0,
             0.0,
             0,
             0.0,
             1
         )
        return EnvelopePoint(
            index=index,
            time=time,
            value=value,
            shape=shape,
            tension=tension,
            selected=selected,
        )

    @property
    def has_valid_id(self) -> bool:
        """
        Whether ReaScript ID is still valid.

        For instance, if envelope has been deleted, ID will not be valid
        anymore.

        :type: bool
        """
        return self._has_valid_id_inside()

    @reapy_boost.inside_reaper()
    def _has_valid_id_inside(self) -> bool:
        try:
            project_id = self.parent.project.id
        except (OSError, AttributeError):
            return False
        pointer, name = self._get_pointer_and_name()
        return bool(
            RPR.ValidatePtr2(  # type:ignore
                project_id, pointer, name
            )
        )

    def insert_point(self, point: EnvelopePoint, sort: bool = True) -> bool:
        """Insert EnvelopePoint

        Parameters
        ----------
        point : EnvelopePoint
            index not counted
        sort : bool, optional
            set to False if insert many points,
            than use self.sort_points()

        Returns
        -------
        bool
        """
        (retval, _, _, _, _, _, _, _) = RPR.InsertEnvelopePoint(  # type:ignore
            self.id, point['time'], point['value'], point['shape'],
            point['tension'], point['selected'], not sort
        )
        return retval

    @property
    def items(self) -> ty.List[AutomationItem]:
        """
        List of automation items in envelope.

        :type: list of reapy_boost.AutomationItem
        """
        items = [
            reapy_boost.AutomationItem(self, i) for i in range(self.n_items)
        ]
        return items

    @property
    def n_items(self) -> int:
        """
        Number of automation items in envelope.

        :type: int
        """
        n_items = RPR.CountAutomationItems(self.id)  # type:ignore
        return n_items

    @property
    def n_points(self) -> int:
        """
        Number of points in envelope.

        :type: int
        """
        n_points = RPR.CountEnvelopePoints(self.id)  # type:ignore
        return n_points

    @property
    def name(self) -> str:
        """
        Envelope name.

        :type: str
        """
        name = RPR.GetEnvelopeName(self.id, "", 2048)[2]  # type:ignore
        return name

    @property
    def parent(self) -> ty.Union[Track, Take]:
        """
        Envelope parent.

        :type: Take or Track
        """
        return self._parent

    def set_point(
        self, index: int, value: EnvelopePoint, sort: bool = True
    ) -> bool:
        """Set envelope point.

        Note
        ----
        Not tested yet

        Parameters
        ----------
        index : int
        value : EnvelopePoint
        sort : bool, optional
            set to False if set many points,
            than use self.sort_points()
        """
        (retval, _, _, _, _, _, _, _, _) = RPR.SetEnvelopePoint(  # type:ignore
            self.id, index, value['time'], value['value'], value['shape'],
            value['tension'], value['selected'], not sort
        )
        return bool(retval)

    def sort_points(self) -> None:
        RPR.Envelope_SortPoints(self.id)  # type:ignore


class EnvelopeList(ReapyObject):
    """
    Container class for the list of envelopes on a Take or Track.

    Envelopes can be accessed from the EnvelopeList either by index,
    name or chunk_name (e.g. "<VOLENV").

    Examples
    --------
    >>> len(track.envelopes)
    2
    >>> envelope = track.envelopes[0]
    >>> envelope.name
    'Volume'
    >>> envelope == track.envelopes["Volume"]
    True
    >>> envelope == track.envelopes["<VOLENV"]
    True
    >>> [e.name for e in track.envelopes]
    ['Volume', 'Pan']
    """

    def __init__(self, parent: ty.Union[Track, Take]):
        self.parent = parent

    @property
    def _args(self) -> ty.Tuple[ty.Union[Track, Take]]:
        return (self.parent, )

    def __getitem__(self, key: ty.Union[str, int]) -> Envelope:
        parent_type = self.parent.__class__._reapy_parent.__name__
        attr = "Get{}Envelope".format(parent_type)
        if isinstance(key, str):
            if key.startswith("<") and parent_type == 'Track':
                attr += "ByChunkName"
            else:
                attr += "ByName"
        callback = getattr(RPR, attr)
        envelope = Envelope(self.parent, callback(self.parent.id, key))
        if not envelope._is_defined:
            raise KeyError("No envelope for key {}".format(repr(key)))
        return envelope

    def __len__(self) -> int:
        return self.parent.n_envelopes
