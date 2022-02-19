from typing import Dict, Optional
from reapy_boost import reascript_api as RPR
from reapy_boost.core import ReapyObject
import reapy_boost


class AutomationItem(ReapyObject):

    _class_name = "AutomationItem"

    def __init__(
        self,
        envelope: Optional['reapy_boost.Envelope'] = None,
        index: int = 0,
        envelope_id: int = None
    ) -> None:
        if envelope is not None:
            envelope_id = envelope.id
        if envelope_id is None:
            raise TypeError(
                'Either envelope or envelope_id has to be specified'
            )
        self.envelope_id = envelope_id
        self.index = index

    @property
    def _kwargs(self) -> Dict[str, int]:
        return {"index": self.index, "envelope_id": self.envelope_id}

    def delete_points_in_range(self, start: float, end: float) -> None:
        """
        Delete points between `start` and `end`.

        Parameters
        ----------
        start : float
            Range start in seconds.
        end : float
            Range end in seconds.
        """
        RPR.DeleteEnvelopePointRangeEx(  # type:ignore
            self.envelope_id, self.index, start, end
        )

    @property
    def length(self) -> float:
        """
        Return item length in seconds.

        Returns
        -------
        length : float
            Item length in seconds.
        """
        length = RPR.GetSetAutomationItemInfo(  # type:ignore
            self.envelope_id, self.index, "D_LENGTH", 0, False
        )
        return length

    @length.setter
    def length(self, length: float) -> None:
        """
        Set item length.

        Parameters
        ----------
        length : float
            New item length in seconds.
        """
        success = RPR.GetSetAutomationItemInfo(  # type:ignore
            self.envelope_id, self.index, "D_LENGTH", length, True
        )

    @property
    def n_points(self) -> int:
        """
        Return number of automation points in item.

        Returns
        -------
        n_points : int
            Number of automation points in item.
        """
        n_points = RPR.CountEnvelopePointsEx(  # type:ignore
            self.envelope_id, self.index)
        return n_points

    @property
    def pool(self) -> int:
        """
        Return item pool.

        Returns
        -------
        pool : int
            Item pool.
        """
        pool = RPR.GetSetAutomationItemInfo(  # type:ignore
            self.envelope_id, self.index, "D_POOL", 0, False
        )
        return pool

    @pool.setter
    def pool(self, pool: int) -> None:
        """
        Set item pool.

        Parameters
        ----------
        pool : int
            New item pool.
        """
        success = RPR.GetSetAutomationItemInfo(  # type:ignore
            self.envelope_id, self.index, "D_POOL", pool, True
        )

    @property
    def position(self) -> float:
        """
        Return item position in seconds.

        Returns
        -------
        position : float
            Item position in seconds.
        """
        position = RPR.GetSetAutomationItemInfo(  # type:ignore
            self.envelope_id, self.index, "D_POSITION", 0, False
        )
        return position

    @position.setter
    def position(self, position: float) -> None:
        """
        Set item position.

        Parameters
        ----------
        position : float
            New item position in seconds.
        """
        success = RPR.GetSetAutomationItemInfo(  # type:ignore
            self.envelope_id, self.index, "D_POSITION", position, True
        )
