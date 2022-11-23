"""Define tools such as Program and custom json module."""

import reapy_boost
from ._inside_reaper import inside_reaper, dist_api_is_enabled
from .network.machines import connect, connect_to_default_machine, reconnect, Host, LOCALHOST
from .extension_dependency import (depends_on_sws, depends_on_extension,
                                   generate_imgui)

__all__ = [
    "inside_reaper", "dist_api_is_enabled", "connect",
    "connect_to_default_machine", "reconnect", "depends_on_sws",
    "depends_on_extension", "generate_imgui", "Host", "LOCALHOST"
]