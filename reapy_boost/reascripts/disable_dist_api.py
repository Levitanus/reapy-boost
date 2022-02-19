"""
Disable ```reapy_boost`` distant API.

Running this ReaScript from inside REAPER disables ``reapy_boost`` imports
from outside. It deletes the persistent Web Interface and removes the
ReaScript ``reapy_boost.reascripts.activate_reapy_server`` from the Actions
list.

See also
--------
reapy_boost.reascripts.enable_dist_api
"""

if __name__ == "__main__":
    import reapy_boost
    reapy_boost.config.disable_dist_api()
