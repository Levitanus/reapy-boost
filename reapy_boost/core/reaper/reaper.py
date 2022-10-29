import codecs
import pickle
from types import TracebackType
from typing import Dict, Generic, List, Optional, Tuple, TypeVar, Union
import reapy_boost
import reapy_boost.reascript_api as RPR
import contextlib
from .defer import ReaperConsole

import collections
import io
import os
import sys

_ORIGINAL_PRINT = print


def add_project_tab(
        make_current_project: bool = True) -> 'reapy_boost.Project':
    """Open new project tab and return it.

    Parameters
    ----------
    make_current_project : bool
        Whether to select new project as current project
        (default=`True`).

    Returns
    -------
    project : Project
        New project.
    """
    if not make_current_project:
        current_project = reapy_boost.Project()
        project = add_project_tab(make_current_project=True)
        current_project.make_current_project()
        return project
    perform_action(40859)
    return reapy_boost.Project()


def add_reascript(path: str, section_id: int = 0, commit: bool = True) -> int:
    """
    Add a ReaScript and return the new action ID.

    Parameters
    ----------
    path : str
        Path to script.
    section_id : int, optional (default=0, corresponds to main section).
        Action section ID to which the script must be added.
    commit : bool, optional
        Whether to commit change. Use it when adding a single script.
        You can optimize bulk adding `n` scripts by setting
        `commit=False` for the first `n-1` calls and `commit=True` for
        the last call.

    Returns
    -------
    action_id : int
        New ReaScript action ID.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    path = os.path.abspath(path)
    action_id = RPR.AddRemoveReaScript(  # type:ignore
        True, section_id, path, commit)
    if action_id == 0:
        message = "Script at {} wasn't successfully added.".format(path)
        raise ValueError(message)
    return action_id


def arm_command(command_id: int, section: str = "") -> None:
    """
    Arm or disarm command.

    Parameters
    ----------
    command_id : int
        Command ID. If 0, disarm command.
    section : str, optional
        Command section. Empty string for main section. Default="".
        TODO: explain what section parameter corresponds to.
    """
    RPR.ArmCommand(command_id, section)  # type:ignore


def browse_for_file(window_title: str = "",
                    extension: str = "") -> Optional[str]:
    """
    Ask the user to select a file.

    Parameters
    ----------
    window_title : str, optional
        Window title (default="")
    extension : str, optional
        Extension for file (e.g. "mp3", "txt"...) (default=all types).

    Returns
    -------
    path : str or NoneType
        Path to file, or None if user cancelled.
    """
    success, path, *_ = RPR.GetUserFileNameForRead(  # type:ignore
        "", window_title, extension)
    if success:
        return path


def clear_console() -> None:
    """
    Clear Reaper console.

    See also
    --------
    ReaProject.show_console_message
    """
    RPR.ClearConsole()  # type:ignore


def clear_peak_cache() -> None:
    """
    Reset global peak cache.
    """
    RPR.ClearPeakCache()  # type:ignore


def dB_to_slider(db: float) -> float:
    """
    Convert decibel value to slider.

    Parameters
    ----------
    db : float
        Decibel value.

    Returns
    -------
    slider : float
        Slider value.

    See also
    --------
    slider_to_dB
    """
    slider = RPR.DB2SLIDER(db)  # type:ignore
    return slider


def delete_ext_state(section: str, key: str, persist: bool = False) -> None:
    """
    Delete extended state value for a given section and key.

    Parameters
    ----------
    section : str
        Extended state section.
    key : str
        Extended state key.
    persist : bool
        Whether extended state should remain deleted next time REAPER
        is opened.
    """
    RPR.DeleteExtState(section, key, persist)  # type:ignore


def disarm_command() -> None:
    """
    Disarm command.
    """
    arm_command(0)


def get_armed_command() -> Optional[Tuple[int, str]]:
    command_id, section, _ = RPR.GetArmedCommand("", 2048)  # type:ignore
    if command_id == 0:
        return
    return command_id, section


def get_command_id(command_name: str) -> Optional[int]:
    """
    Return ID of command with a given name.

    Parameters
    ----------
    command_name : str
        Command name. Perhaps, id-string

    Returns
    -------
    command_id : int or None
        Command ID, or None if name can't be found.
    """
    command_id = RPR.NamedCommandLookup(command_name)  # type:ignore
    command_id = command_id if command_id else None
    return command_id


def get_command_name(command_id: int) -> str:
    """
    Return name of command with a given ID.

    Parameters
    ----------
    command_id : int
        Command ID.

    Returns
    -------
    command_name : str, None
        Command name, or None for a native command.
    """
    command_name = RPR.ReverseNamedCommandLookup(command_id)  # type:ignore
    if command_name is not None:
        command_name = "_" + command_name
    return command_name


def get_exe_dir() -> str:
    """
    Return REAPER.exe directory (e.g. "C:\\Program Files\\REAPER").

    Returns
    -------
    path : str
        Path to REAPER.exe directory.
    """
    path = RPR.GetExePath()  # type:ignore
    return path


def get_ext_state(section: str,
                  key: str,
                  pickled: bool = False) -> Union[str, object]:
    """
    Get the extended state value for a specific section and key.

    Parameters
    ----------
    section : str
        Extended state section.
    key : str
        Extended state key for section `section`.
    pickled: bool
        Whether data was pickled or not.

    Returns
    -------
    value : str
        Extended state value.

    See also
    --------
    delete_ext_state
    set_ext_state
    """
    value = RPR.GetExtState(section, key)  # type:ignore
    if value and pickled:
        value = pickle.loads(codecs.decode(value.encode(), "base64"))
    return value


def get_global_automation_mode() -> str:
    """
    Return global automation override mode.

    Returns
    -------
    override_mode : str
        One of the following values:
            "bypass"
            "latch"
            "none"
            "read"
            "touch"
            "trim/read"
            "write"
    TODO: consider introducing of Enum
    """
    modes = {
        -1: "none",
        0: "trim/read",
        1: "read",
        2: "touch",
        3: "write",
        4: "latch",
        5: "bypass"
    }
    override_mode = modes[RPR.GetGlobalAutomationOverride()]  # type:ignore
    return override_mode


def get_ini_file() -> str:
    """
    Return path to REAPER.ini file.

    Returns
    -------
    path : str
        Path to REAPER.ini file.
    """
    path = RPR.get_ini_file()  # type:ignore
    return path


def get_last_touched_track() -> Optional['reapy_boost.Track']:
    """
    Return last touched track, or None if no track has been touched.

    Returns
    -------
    track : Track or None if no track has been touched.
    """
    track = reapy_boost.Track(RPR.GetLastTouchedTrack())  # type:ignore
    if not track._is_defined:
        track = None
    return track


def get_main_window() -> 'reapy_boost.Window':
    """
    Return main window.

    Returns
    -------
    window : Window
        Main window.
    """
    window = reapy_boost.Window(RPR.GetMainHwnd())  # type:ignore
    return window


@reapy_boost.inside_reaper()
def get_projects() -> List['reapy_boost.Project']:
    """
    Return list of all opened projects.

    Returns
    -------
    projects : list of Project
        List of all projects.
    """
    i, projects = 0, [reapy_boost.Project(index=0)]
    while projects[-1]._is_defined:
        i += 1
        projects.append(reapy_boost.Project(index=i))
    projects.pop()
    return projects


def get_reaper_version() -> str:
    version = RPR.GetAppVersion()  # type:ignore
    return version


def get_resource_path() -> str:
    """
    Return path to directory where .ini files are stored.

    Returns
    -------
    path : str
        Path to directory where .ini files are stored.
    """
    path = RPR.GetResourcePath()  # type:ignore
    return path


def get_user_inputs(title: str,
                    captions: List[str],
                    retvals_size: int = 1024) -> Dict[str, str]:
    """Show text inputs to user and get values from them.

    Parameters
    ----------
    title : str
        Popup title.
    captions : List[str]
        Names of input fields.
    retvals_size : int, optional
        Maximum number of characters that will be retrieved for each
        field. User may enter more, but only the first `retvals_size`
        will be returned. (default=1024)

    Returns
    -------
    Dict[str,str]
        Dictionary of pairs {caption: response}.

    Raises
    ------
    RuntimeError
        When user clicked the Cancel button.
    """
    success, _, _, _, retvals_csv, _ = RPR.GetUserInputs(  # type:ignore
        title, len(captions), ",".join(captions), "", retvals_size)
    if success:
        return dict(zip(captions, retvals_csv.split(",")))
    else:
        raise RuntimeError('User clicked Cancel.')


def has_ext_state(section: str, key: str) -> bool:
    """
    Return whether extended state exists for given section and key.

    Parameters
    ----------
    section : str
        Extended state section.
    key : str
        Extended state key.

    Returns
    -------
    has_ext_state : bool
    """
    has_ext_state = bool(RPR.HasExtState(section, key))  # type:ignore
    return has_ext_state


def is_valid_id(id_: str) -> bool:
    """If it is not nullptr.

    Parameters
    ----------
    id_ : str

    Notes
    -----
    Not actually does anything else than id is not 0x00000

    Returns
    -------
    bool
    """
    return not id_.endswith("0x0000000000000000")


@reapy_boost.inside_reaper()
def open_project(filepath: str,
                 in_new_tab: bool = False,
                 make_current_project: bool = True) -> 'reapy_boost.Project':
    """
    Open project and return it.

    Parameters
    ----------
    filepath : str
    in_new_tab : bool, optional
        Whether to open project in new tab (default=`False`).
    make_current_project : bool, optional
        Whether to make opened project current project (has no effect
        if `in_new_tab` is `False`).

    Returns
    -------
    project : Project
        Opened project.
    """
    if not make_current_project:
        current_project = reapy_boost.Project()
    if in_new_tab:
        add_project_tab(make_current_project=True)
    RPR.Main_openProject(filepath)  # type:ignore
    project = reapy_boost.Project()
    if not make_current_project:
        current_project.make_current_project()
    return project


def perform_action(action_id: int) -> None:
    """
    Perform action with ID `action_id` in the main Actions section.

    Parameters
    ----------
    action_id : int
        Action ID in the main Actions section.
    """
    RPR.Main_OnCommand(action_id, 0)  # type:ignore


class prevent_ui_refresh(contextlib.ContextDecorator):
    """Class to prevent UI refresh on certain pieces of code.

    Its instance can be used both as decorator and as context manager:

    >>> with reapy_boost.prevent_ui_refresh():
    ...     reapy_boost.Project.add_track()

    >>> @prevent_ui_refresh()
    >>> def some_function(*args, **kwargs):
    ...     reapy_boost.Project.add_track()

    """

    def __enter__(self) -> None:
        RPR.PreventUIRefresh(1)  # type:ignore

    def __exit__(self, exc_type: Exception, exc_val: str,
                 exc_tb: TracebackType) -> None:
        RPR.PreventUIRefresh(-1)  # type:ignore


def print(*args: object, **kwargs: object) -> None:
    """
    Alias to ReaProject.show_console_message.
    """
    show_console_message(*args, **kwargs)


class reaprint(contextlib.ContextDecorator):
    """Class to send all prints to ReaperConsole.

    Its instance can be used both as decorator and context manager:

    >>> with reapy_boost.reaprint():
    ...     print('This will go to the console!')
    ...     print('All these contexted will go to the console!')

    >>> @reapy_boost.reaprint()
    >>> def some_function(*args, **kwargs):
    ...     print('This will go to the console!')
    ...     print('All these decorated prints will go to the console!')

    """
    _original_stdouts = collections.deque()

    def __enter__(self) -> None:
        self._original_stdouts.append(sys.stdout)
        sys.stdout = ReaperConsole()

    def __exit__(self, exc_type: Exception, exc_val: str,
                 exc_tb: TracebackType) -> None:
        sys.stdout = self._original_stdouts.pop()


def remove_reascript(path: str,
                     section_id: int = 0,
                     commit: bool = True) -> None:
    """
    Remove a ReaScript.

    Parameters
    ----------
    path : str
        Path to script.
    section_id : int, optional (default=0, corresponds to main section).
        Action section ID to which the script must be added.
    commit : bool, optional
        Whether to commit change. Use it when removing a single script.
        You can optimize bulk removing `n` scripts by setting
        `commit=False` for the first `n-1` calls and `commit=True` for
        the last call.
    """
    path = os.path.abspath(path)
    success = RPR.AddRemoveReaScript(  # type:ignore
        False, section_id, path, commit)
    if not success:
        message = "Script at {} wasn't successfully added.".format(path)
        raise ValueError(message)


def rgb_from_native(native_color: int) -> Tuple[int, int, int]:
    """
    Extract RGB values from a native (OS-dependent) color.

    Parameters
    ----------
    native_color : int
        Native color.

    Returns
    -------
    r, g, b : (int, int, int)
        RGB values between 0 and 255.
    """
    _, r, g, b = RPR.ColorFromNative(native_color, 0, 0, 0)  # type:ignore
    return r, g, b


def rgb_to_native(rgb: Tuple[int, int, int]) -> int:
    """
    Make a native (OS-dependent) color from RGB values.

    Parameters
    ----------
    rgb : (int, int, int)
        RGB triplet of integers between 0 and 255.

    Returns
    -------
    native_color : int
        Native color.
    """
    native_color = RPR.ColorToNative(*rgb)  # type:ignore
    return native_color


def set_ext_state(section: str,
                  key: str,
                  value: Union[str, object],
                  persist: bool = False,
                  pickled: bool = False) -> None:
    """
    Set the extended state value for a specific section and key.

    Parameters
    ----------
    section : str
        Extended state section.
    key : str
        Extended state key for section `section`.
    value : Union[Any, str]
        State value. Will be dumped to str using `pickle` if
        `pickled` is `True`. Length of the dumped value
        must not be over 2**31 - 2.
    persist : bool
        Whether the value should be stored and reloaded the next time
        REAPER is opened.
    pickled : bool, optional
        Data will be pickled with the last version if True.
        If you using mypy as type checker, typing_extensions.Literal[True]
        has to be used for `pickled`.    
        
    Raises
    ------
    ValueError
        If dumped `value` has length over 2**31 - 2.

    See also
    --------
    delete_ext_state
    get_ext_state
    """
    if pickled:
        value = pickle.dumps(value)
        value = codecs.encode(value, "base64").decode()
    if not isinstance(value, (str, bytes)):
        raise TypeError("value has to be of type 'str', or should be picked")
    if len(value) > 2**31 - 2:
        message = ("Dumped value length is {:,d}. It must not be over "
                   "2**31 - 2.")
        raise ValueError(message.format(len(value)))
    RPR.SetExtState(section, key, value, persist)  # type:ignore


def set_global_automation_mode(mode: str) -> None:
    """
    Set global automation mode.

    Parameters
    ----------
    mode : str
        One of the following values:
            "bypass"
            "latch"
            "none"
            "read"
            "touch"
            "trim/read"
            "write"
    TODO: consider introducing Enum
    """
    modes = {
        "none": -1,
        "trim/read": 0,
        "read": 1,
        "touch": 2,
        "write": 3,
        "latch": 4,
        "bypass": 5
    }
    RPR.SetGlobalAutomationOverride(modes[mode])  # type:ignore


def show_console_message(*args: object, sep: str = " ", end: str = "\n"):
    """
    Print a message to the Reaper console.

    Parameters
    ----------
    args : tuple
        Values to print.
    sep : str, optional
        String inserted between values (default=" ").
    end : str, optional
        String appended after the last value (default="\n").
    """
    file = io.StringIO()
    _ORIGINAL_PRINT(*args, sep=sep, end=end, file=file)
    file.seek(0)
    txt = file.read()
    RPR.ShowConsoleMsg(txt)  # type:ignore


def show_message_box(text: str = "", title: str = "", type: str = "ok"):
    """
    Show message box.

    Parameters
    ----------
    text : str
        Box message
    title : str
        Box title
    type : str
        One of the following values.

        "ok"
        "ok-cancel"
        "abort-retry-ignore"
        "yes-no-cancel"
        "yes-no"
        "retry-cancel"

    Returns
    -------
    status : str
        One of the following values.

        "ok"
        "cancel"
        "abort"
        "retry"
        "ignore"
        "yes"
        "no"
    """
    all_types = {
        "ok": 0,
        "ok-cancel": 1,
        "abort-retry-ignore": 2,
        "yes-no-cancel": 3,
        "yes-no": 4,
        "retry-cancel": 5
    }
    all_status = {
        1: "ok",
        2: "cancel",
        3: "abort",
        4: "retry",
        5: "ignore",
        6: "yes",
        7: "no"
    }
    status = RPR.ShowMessageBox(  # type:ignore
        text, title, all_types[type])
    status = all_status[status]
    return status


def slider_to_dB(slider: float) -> float:
    """
    Convert slider value to decibel.

    Parameters
    ----------
    slider : float
        Slider value.

    Returns
    -------
    db : float
        Decibel value.

    See also
    --------
    dB_to_slider
    """
    db = RPR.SLIDER2DB(slider)  # type:ignore
    return db


def test_api() -> None:
    """Display a message window if the API can successfully be called."""
    RPR.APITest()  # type:ignore


class undo_block(contextlib.ContextDecorator):
    """Class to register undo block.

    Its instance can be used both as decorator and context manager:

    >>> with reapy_boost.undo_block('add track'):
    ...     reapy_boost.Project.add_track()

    >>> @reapy_boost.undo_block('add track')
    >>> def some_function(*args, **kwargs):
    ...     reapy_boost.Project.add_track()

    :param undo_name: Str to register undo name (shown later in Undo menu)
    :param flags: Int to pass to Undo_EndBlock
                    (leave default if you don't know what it is)
        1: track configurations
        2: track FX
        4: track items
        8: project states
        16: freeze states
    """

    def __init__(self, undo_name: str, flags: int = -1) -> None:
        self.undo_name = undo_name
        self.flags = flags

    def __enter__(self) -> None:
        RPR.Undo_BeginBlock()  # type:ignore

    def __exit__(self, exc_type: Exception, exc_val: str,
                 exc_tb: TracebackType) -> None:
        RPR.Undo_EndBlock(self.undo_name, self.flags)  # type:ignore


def update_arrange() -> None:
    """
    Redraw the arrange view.
    """
    RPR.UpdateArrange()  # type:ignore


def update_timeline() -> None:
    """
    Redraw the arrange view and ruler.
    """
    RPR.UpdateTimeline()  # type:ignore


def view_prefs() -> None:
    """
    Open Preferences.
    """
    RPR.ViewPrefs(0, "")  # type:ignore


T = TypeVar("T")


class ExtState(Generic[T]):
    """Generalized External state item.

    Parameters
    ----------
    section : str
    key : str
    value : Optional[T]
        any value, that can be pickled
    persist : bool
        If value should be saved between sessions.
        Note, that it will delete value at initialization.
    pickled : bool, optional
        Wether value should be pickled.
    project : Optional[reapy_boost.Project], optional
        If specified, value will be stored in project file.
        
    Raises
    ------
    reapy_boost.errors.InvalidObjectError
        if project is invalid object
        
    Usage
    -----
    >>> state = reapy_boost.ExtState("my section", "my value", 5)
    ... print(state.value)  # 5
    ... state.value = 3
    ... print(state.value)  # 3
    ... del state.value
    ... print(state.value)  # None
    """

    def __init__(self,
                 section: str,
                 key: str,
                 value: Optional[T],
                 persist: bool = True,
                 pickled: bool = True,
                 project: Optional[reapy_boost.Project] = None) -> None:
        self.section = section
        self.key = key
        self.persist = persist
        self.pickled = pickled
        self.project = project
        if value is not None:
            if persist and self.value is None:
                self.value = value
        if not persist:
            del self.value

    @property
    def value(self) -> Optional[T]:
        if self.project is None:
            return self._value_from_reaper()
        return self._value_from_project()

    @value.setter
    def value(self, value: T) -> None:
        if self.project is None:
            return self._value_to_reaper(value)
        return self._value_to_project(value)

    @value.deleter
    def value(self) -> None:
        if self.project is None:
            delete_ext_state(self.section, self.key)
            return
        project = self._check_project()
        project.set_ext_state(self.section, self.key, "", False)

    def _value_to_reaper(self, value: T) -> None:
        set_ext_state(self.section, self.key, value, self.persist, self.pickled)

    def _value_to_project(self, value: T) -> None:
        project = self._check_project()
        project.set_ext_state(self.section, self.key, value, self.pickled)

    def _value_from_reaper(self) -> Optional[T]:
        if not has_ext_state(self.section, self.key):
            return None
        return get_ext_state(self.section, self.key,
                             self.pickled)  # type:ignore

    def _value_from_project(self) -> Optional[T]:
        project = self._check_project()
        value = project.get_ext_state(self.section, self.key, self.pickled)
        return None if not value else value  # type:ignore

    def _check_project(self) -> reapy_boost.Project:
        if self.project is None or not self.project.has_valid_id:
            raise reapy_boost.errors.InvalidObjectError(self.project)
        return self.project
