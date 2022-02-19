from typing import Dict, Optional, Tuple
import reapy_boost
from reapy_boost import reascript_api as RPR
from reapy_boost.core import ReapyObject


class TimeSelection(ReapyObject):

    _class_name = "TimeSelection"

    def __init__(
        self,
        parent_project: Optional['reapy_boost.Project'] = None,
        parent_project_id: Optional[str] = None
    ):
        if parent_project_id is None:
            message = (
                "One of `parent_project` or `parent_project_id` must be "
                "specified."
            )
            assert parent_project is not None, message
            parent_project_id = parent_project.id
        self.project_id: str = parent_project_id

    def _get_infos(self) -> Tuple[str, bool, bool, float, float, bool]:
        """
        Return infos as returned by RPR.GetSet_LoopTimeRange2.

        Returns
        -------
        infos : tuple
            str: proj_id
            bool: isSet (False)
            bool: isLoop
            float: start
            float: end
            bool: allowautoseek
        """
        infos = RPR.GetSet_LoopTimeRange2(  # type:ignore
            self.project_id, False, False, 0, 0, False
        )
        return infos  # type:ignore

    def _set_start_end(
        self,
        start: Optional[float] = None,
        end: Optional[float] = None
    ) -> None:
        infos = list(
            RPR.GetSet_LoopTimeRange2(  # type:ignore
                self.project_id, False, False, 0, 0, False
            )
        )
        if start is None:
            start = infos[3]
        if end is None:
            end = infos[4]
        infos[1], infos[3], infos[4] = True, start, end
        RPR.GetSet_LoopTimeRange2(*infos)  # type:ignore

    @property
    def _kwargs(self) -> Dict[str, str]:  # type:ignore
        return {"parent_project_id": self.project_id}

    @property
    def end(self) -> float:
        """
        Return time selection end in seconds.

        Returns
        -------
        end : float
            Time selection end in seconds.
        """
        return self._end_inside()

    @reapy_boost.inside_reaper()
    def _end_inside(self) -> float:
        infos = self._get_infos()
        end = infos[4]
        return end

    @end.setter
    def end(self, end: float) -> None:
        """
        Set time selection end.

        Parameters
        ----------
        end : float
            Time selection end in seconds.
        """
        self._set_start_end(end=end)

    @property
    def is_looping(self) -> bool:
        """
        Return whether looping is enabled.

        Returns
        -------
        looping : bool
            Whether looping is enabled.
        """
        is_looping = bool(
            RPR.GetSetRepeatEx(  # type:ignore
                self.project_id, -1
            )
        )
        return is_looping

    @is_looping.setter
    def is_looping(self, is_looping: bool) -> None:
        """
        Sets whether time selection should loop.

        Parameters
        ----------
        looping : bool
            Whether time selection should loop.
        """
        if is_looping:
            self.loop()
        else:
            self.unloop()

    @property
    def length(self) -> float:
        """
        Return time selection length in seconds.

        Returns
        -------
        length : float
            Time selection length in seconds.
        """
        return self._length_inside()

    @reapy_boost.inside_reaper()
    def _length_inside(self) -> float:
        infos = self._get_infos()
        start, end = infos[3:5]
        length = end - start
        return length

    @length.setter
    def length(self, length: float) -> None:
        """
        Set time selection length (by moving its end).

        Parameters
        ----------
        length : float
            Time selection length in seconds.
        """
        infos = list(
            RPR.GetSet_LoopTimeRange2(  # type:ignore
                self.project_id, False, False, 0, 0, False
            )
        )
        infos[1], infos[4] = True, infos[3] + length
        RPR.GetSet_LoopTimeRange2(*infos)  # type:ignore

    def loop(self) -> None:
        """
        Enable time selection looping.

        See also
        --------
        TimeSelection.is_looping
        TimeSelection.unloop
        """
        RPR.GetSetRepeatEx(self.project_id, 1)  # type:ignore

    @property
    def start(self) -> float:
        """
        Return time selection start in seconds.

        Returns
        -------
        start : float
            Time selection start in seconds.
        """
        return self._start_inside()

    @reapy_boost.inside_reaper()
    def _start_inside(self) -> float:
        infos = self._get_infos()
        start = infos[3]
        return start

    @start.setter
    def start(self, start: float) -> None:
        """
        Set time selection start.

        Parameters
        ----------
        start : float
            New time selection start.
        """
        self._set_start_end(start)

    def shift(self, direction: str = "") -> None:
        """
        Shift time selection.

        Parameters
        ----------
        direction : {"right", "left"}
            Direction to which time selection will be shifted. Nothing
            happens if direction is neither "right" nor "left". Note
            that the shift size depends on whether snap is enabled
            and of the zoom level.
        """
        if direction == "right":
            RPR.Loop_OnArrow(self.project_id, 1)  # type:ignore
        elif direction == "left":
            RPR.Loop_OnArrow(self.project_id, -1)  # type:ignore

    def unloop(self) -> None:
        """
        Disable time selection looping.

        See also
        --------
        TimeSelection.is_looping
        TimeSelection.loop
        """
        RPR.GetSetRepeatEx(self.project_id, 0)  # type:ignore
