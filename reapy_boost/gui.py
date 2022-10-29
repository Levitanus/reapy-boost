from abc import abstractmethod
from typing import Any, Callable, Dict, Generator, Iterator, List, NewType, Sequence, Union, cast
from enum import IntFlag

from typing import Optional
import reapy_boost as rpr
from reapy_boost import ImGui

_EXT_SECTION = "reapy_boost_GUI"
_EXT_PERSIST = True

ImGuiContext = NewType("ImGuiContext", str)


class Widget:

    @abstractmethod
    def frame(self, ctx: ImGuiContext) -> None:
        ...

    def offset_from_start_x(self, offset: int) -> 'Widget':
        """Set x offset to use in Row()

        Parameters
        ----------
        offset : int
            in

        Returns
        -------
        Widget
            self
        """
        setattr(self, '_offset_from_start_x', offset)
        return self


class Content(Widget):

    def __init__(self, *widgets: Widget) -> None:
        self.widgets = widgets

    def frame(self, ctx: ImGuiContext) -> None:
        for widget in self.widgets:
            widget.frame(ctx)


class Window:

    def __init__(self, name: str, content: Content) -> None:
        if not rpr.is_inside_reaper():
            raise rpr.errors.OutsideREAPERError(
                "Currently, gui can be used only from inside REAPER.")
        self.name = name
        self.content = content
        self.ctx: ImGuiContext = ImGui.CreateContext(
            label=self.name,
            config_flagsInOptional=ImGui.ConfigFlags_DockingEnable())
        self.docked = rpr.ExtState(_EXT_SECTION,
                                   f'{self.name}_dock_state',
                                   False,
                                   persist=_EXT_PERSIST)
        self.dock_id = rpr.ExtState(_EXT_SECTION,
                                    f'{self.name}_dock_id',
                                    0,
                                    persist=_EXT_PERSIST)

    def dock_flag(self, docked: bool) -> int:
        if docked:
            return 0
        return cast(int, ImGui.WindowFlags_NoDocking())

    def before_begin(self) -> int:
        if docked := self.docked.value:
            if self.dock_id.value == 0:
                self.dock_id.value = -2
                ImGui.SetNextWindowDockID(self.ctx, self.dock_id.value)
        return self.dock_flag(docked or False)

    def frame(self) -> bool:
        window_flags = self.before_begin(
        ) | ImGui.WindowFlags_AlwaysAutoResize()
        visible, opened = ImGui.Begin(self.ctx, self.name, True, window_flags)

        if visible:
            if self.docked.value:
                self.dock_id.value = ImGui.GetWindowDockID(self.ctx)
            self.content.frame(self.ctx)
        if visible:
            ImGui.End(self.ctx)
        return cast(bool, opened)

    def run(self) -> None:
        opened = self.frame()
        if opened:
            rpr.defer(self.run)
        else:
            ImGui.DestroyContext(self.ctx)


ImGuiControlFunc = Callable[[], None]


class Row(Content):

    def __init__(self,
                 *widgets: Widget,
                 spacing: Optional[int] = None) -> None:
        super().__init__(*widgets)
        self.spacing = spacing

    def frame(self, ctx: ImGuiContext) -> None:
        for idx, widget in enumerate(self.widgets):
            widget.frame(ctx)
            if idx < len(self.widgets) - 1:
                if hasattr(widget, "_offset_from_start_x"):
                    x_offset = getattr(widget, "_offset_from_start_x")
                else:
                    x_offset = None
                ImGui.SameLine(ctx, x_offset, self.spacing)


class Button(Widget):

    def __init__(self, text: str) -> None:
        self.text = text
        self.on_click: Optional[ImGuiControlFunc] = None
        self._width: Optional[int] = None
        self._height: Optional[int] = None

    def width(self, width: int) -> 'Button':
        self._width = width
        return self

    def height(self, height: int) -> 'Button':
        self._height = height
        return self

    def set_click(self, func: ImGuiControlFunc) -> 'Button':
        self.on_click = func
        return self

    def frame(self, ctx: ImGuiContext) -> None:
        if ImGui.Button(ctx, self.text, self._width,
                        self._height) and self.on_click is not None:
            self.on_click()


class CheckBox(Widget):

    def __init__(self,
                 text: str,
                 state: Optional['rpr.ExtState[bool]'] = None) -> None:
        self.text = text
        self.state = state
        self.on_click: Optional[Callable[[bool], None]] = None
        self._value: Optional[bool] = None

    def set_value(self, value: bool) -> 'CheckBox':
        self._value = value
        return self

    def frame(self, ctx: ImGuiContext) -> None:
        if self._value is not None:
            in_value = self._value
        elif self.state is None:
            in_value = False
        else:
            in_value = self.state.value or False
        rt, value = ImGui.Checkbox(ctx, self.text, in_value)
        if rt:
            if self.state is not None:
                self.state.value = value
            elif self.on_click is not None:
                self.on_click(value)

    def set_click(self, fn: Callable[[bool], None]) -> 'CheckBox':
        self.on_click = fn
        return self


class Text(Widget):

    def __init__(self, text: str) -> None:
        self.text = text
        self.state: Optional[rpr.ExtState] = None

    def frame(self, ctx: ImGuiContext) -> None:
        if self.state is not None:
            self.text = str(self.state.value) or "no value"
        ImGui.Text(ctx=ctx, text=self.text)


class TableColumnFlag(IntFlag):
    none = ImGui.TableColumnFlags_None()
    default_hide = ImGui.TableColumnFlags_DefaultHide()
    default_sort = ImGui.TableColumnFlags_DefaultSort()
    disabled = ImGui.TableColumnFlags_Disabled()
    indent_disable = ImGui.TableColumnFlags_IndentDisable()
    indent_enable = ImGui.TableColumnFlags_IndentEnable()
    is_enabled = ImGui.TableColumnFlags_IsEnabled()
    is_hovered = ImGui.TableColumnFlags_IsHovered()
    is_sorted = ImGui.TableColumnFlags_IsSorted()
    is_visible = ImGui.TableColumnFlags_IsVisible()
    no_clip = ImGui.TableColumnFlags_NoClip()
    no_header_label = ImGui.TableColumnFlags_NoHeaderLabel()
    no_header_width = ImGui.TableColumnFlags_NoHeaderWidth()
    no_hide = ImGui.TableColumnFlags_NoHide()
    no_reorder = ImGui.TableColumnFlags_NoReorder()
    no_resize = ImGui.TableColumnFlags_NoResize()
    no_sort = ImGui.TableColumnFlags_NoSort()
    no_sort_ascending = ImGui.TableColumnFlags_NoSortAscending()
    no_sort_descending = ImGui.TableColumnFlags_NoSortDescending()
    prefer_sort_ascending = ImGui.TableColumnFlags_PreferSortAscending()
    prefer_sort_descending = ImGui.TableColumnFlags_PreferSortDescending()
    width_fixed = ImGui.TableColumnFlags_WidthFixed()
    width_stretch = ImGui.TableColumnFlags_WidthStretch()


class TableColumn:

    def __init__(self, name: str) -> None:
        self.name = name
        self._flags = TableColumnFlag.none
        self.width = None
        self.user_id = None

    @property
    def flags(self) -> TableColumnFlag:
        return self._flags


class TableRow:

    def __init__(self, columns: Dict[str, Union[str, Widget]]) -> None:
        self._columns = columns

    @property
    def columns(self) -> List[TableColumn]:
        return [TableColumn(cl) for cl in self._columns]

    def frame(self, ctx: ImGuiContext) -> None:
        for idx, name in enumerate(self._columns):
            if ImGui.TableSetColumnIndex(ctx, idx):
                content = self._columns[name]
                if isinstance(content, str):
                    widget: Widget = Text(content)
                else:
                    widget = content
                widget.frame(ctx)


class Table(Widget):

    def __init__(self, name: str, with_clipper: bool = True) -> None:
        self.name = name
        self.with_clipper = with_clipper

    @abstractmethod
    def len(self) -> int:
        ...

    @abstractmethod
    def make_rows(self, start_row: int,
                  end_row: int) -> Generator[TableRow, None, None]:
        ...

    def frame(self, ctx: ImGuiContext) -> None:
        if not ImGui.BeginTable(ctx, self.name, self.len()):
            return

        ImGui.TableSetupScrollFreeze(ctx, 0, 1)

        init_row = list(self.make_rows(0, 1))
        if not init_row:
            return

        self.setup_columns(ctx, init_row[0].columns)
        clipper = ImGui.CreateListClipper(ctx)
        ImGui.ListClipper_Begin(clipper, self.len())
        while ImGui.ListClipper_Step(clipper):
            start, end = ImGui.ListClipper_GetDisplayRange(clipper)
            rows = self.make_rows(start, end)
            for idx, row in enumerate(rows):
                ImGui.TableNextRow(ctx)
                ImGui.PushID(ctx, f"{idx}")
                row.frame(ctx)
                ImGui.PopID(ctx)

        ImGui.EndTable(ctx)

    def setup_columns(self, ctx: ImGuiContext,
                      columns: Sequence[TableColumn]) -> None:
        for column in columns:
            self.setup_column(ctx, column)
        ImGui.TableHeadersRow(ctx)

    def setup_column(self, ctx: ImGuiContext, column: TableColumn) -> None:
        ImGui.TableSetupColumn(ctx, column.name, column.flags, column.width,
                               column.user_id)
