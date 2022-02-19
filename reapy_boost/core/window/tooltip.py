from typing import NoReturn
import reapy_boost.reascript_api as RPR
from .window import Window


class ToolTip(Window):
    """Tooltip window."""
    id: bytes
    _x: int
    _y: int
    _topmost: bool
    _show: bool

    def __init__(
        self,
        message: str = " ",
        x: int = 0,
        y: int = 0,
        topmost: bool = True,
        show: bool = True
    ) -> None:
        """Initialize tooltip.

        Parameters
        ----------
        message : str, optional
            ToolTip message (default=" "). Note that tooltips with
            empty messages are always hidden.
        x : int, optional
            x position (default=0).
        y : int, optional
            y position (default=0).
        topmost : bool, optional
            Whether tooltip should be displayed on top of all other
            windows (default=True).
        show : bool, optional
            Whether to show tooltip on initialization (default=True).
        """
        self._message = message
        self._x = x
        self._y = y
        self._topmost = topmost
        if show:
            self.show()
        self.id = RPR.GetTooltipWindow  # type:ignore

    def hide(self) -> None:
        """Hide tooltip."""
        RPR.TrackCtl_SetToolTip(  # type:ignore
            "", self.x, self.y, self.topmost)
        self._is_shown = False

    @property
    def message(self) -> str:
        """
        Tooltip message.

        Note that tooltips with empty messages are always hidden.

        :type: str
        """
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        self._message = message
        if self._is_shown:
            self.show()

    def refresh(self) -> NoReturn:
        raise NotImplementedError

    def show(self) -> None:
        """Show tooltip."""
        RPR.TrackCtl_SetToolTip(  # type:ignore
            self.message, self.x, self.y, self.topmost)
        self._is_shown = True

    @property
    def topmost(self) -> bool:
        """
        Whether tooltip is displayed on top of all other windows.

        :type: bool
        """
        return self._topmost

    @topmost.setter
    def topmost(self, topmost: bool) -> None:
        self._topmost = topmost
        if self._is_shown:
            self.show()

    @property
    def x(self) -> int:
        """
        x position.

        :type: int"""
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        self._x = x
        if self._is_shown:
            self.show()

    @property
    def y(self) -> int:
        """y position.

        :type: int
        """
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        self._y = y
        if self._is_shown:
            self.show()
