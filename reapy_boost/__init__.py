import sys


def is_inside_reaper() -> bool:
    """
    Return whether ``reapy_boost`` is imported from inside REAPER.

    If ``reapy_boost`` is run from inside a REAPER instance but currently
    controls another REAPER instance on a slave machine (with
    ``reapy_boost.connect``), return False.
    """
    inside = hasattr(sys.modules["__main__"], "obj")
    if not inside:
        return False
    else:
        try:
            return machines.get_selected_machine_host() is None
        except NameError:
            # machines is undefined because we are still in the initial
            # import process.
            return True


from .tools import (
    connect,
    connect_to_default_machine,
    Host,
    LOCALHOST,
    dist_api_is_enabled,
    inside_reaper,
    reconnect,
    generate_imgui,
)
from . import reascript_api, errors
from .config import configure_reaper, add_web_interface
from .core import *
from .core.reaper import *

__version__ = "0.10.2"
__all__ = [
    "reascript_api",
    "JS",
    "errors",
    # config
    "configure_reaper",
    "add_web_interface",
    "Host",
    "LOCALHOST",
    # core.reapy_object
    "ReapyObject",
    "ReapyObjectList",
    # core.project
    "Marker",
    "Project",
    "Region",
    "TimeSelection",
    "MarkerInfo",
    "RegionInfo",
    # core.audio_accessor
    "AudioAccessor",
    # core.envelope
    "Envelope",
    "EnvelopeList",
    "EnvelopePoint",
    # core.fx
    "FX",
    "FXList",
    "FXParam",
    "FXParamsList",
    # core.item
    "Item",
    "MIDIEvent",
    "MIDIEventList",
    "CC",
    "CCList",
    "Note",
    "NoteList",
    "TextSysex",
    "TextSysexInfo",
    "TextSysexList",
    "CCShapeFlag",
    "CCShape",
    "MIDIEventDict",
    "MIDIEventInfo",
    "CCInfo",
    'NoteInfo',
    "Source",
    "Take",
    # core.track
    "AutomationItem",
    "Send",
    "Track",
    "TrackList",
    # core.window
    "MIDIEditor",
    "ToolTip",
    "Window",
    # core.reaper
    'add_reascript',
    'arm_command',
    'browse_for_file',
    'clear_console',
    'clear_peak_cache',
    'dB_to_slider',
    'delete_ext_state',
    'disarm_command',
    'get_armed_command',
    'get_command_id',
    'get_command_name',
    'get_exe_dir',
    'get_ext_state',
    'get_global_automation_mode',
    'get_ini_file',
    'get_last_touched_track',
    'get_main_window',
    'get_projects',
    'get_reaper_version',
    'get_resource_path',
    'get_user_inputs',
    'has_ext_state',
    'is_valid_id',
    'open_project',
    'perform_action',
    'prevent_ui_refresh',
    'print',
    'reaprint',
    'remove_reascript',
    'rgb_from_native',
    'rgb_to_native',
    'set_ext_state',
    'set_global_automation_mode',
    'show_console_message',
    'show_message_box',
    'slider_to_dB',
    'test_api',
    'undo_block',
    'update_arrange',
    'update_timeline',
    'view_prefs',
    'audio',
    'midi',
    'ui',
    'defer',
    'at_exit',
    'ExtState',
    # tools
    'connect',
    'connect_to_default_machine',
    'dist_api_is_enabled',
    'inside_reaper',
    'reconnect',
    'generate_imgui',
]
