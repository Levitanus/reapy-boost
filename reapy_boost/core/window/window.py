from typing import Tuple
import reapy_boost
from reapy_boost.core import ReapyObject
import reapy_boost.reascript_api as RPR


class Window(ReapyObject):

    def __init__(self, id: int) -> None:
        self.id = id

    @property
    def _args(self) -> Tuple[int]:
        return (self.id, )

    def refresh(self) -> None:
        """Refresh window."""
        RPR.DockWindowRefreshForHWND(self.id)  # type:ignore
