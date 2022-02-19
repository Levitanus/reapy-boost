"""
Activate ``reapy_boost`` server.

Running this ReaScript from inside REAPER sets the ``reapy_boost`` server
that receives and executes API calls requests from outside. It will
automatically be run when importing ``reapy_boost`` from outside, if it is
enabled.
"""

import pathlib
import site
import sys

try:
    import reapy_boost
except ImportError:
    reapy_path = pathlib.Path(sys.path[0]).resolve().parent.parent
    sys.path.append(str(reapy_path))
    import reapy_boost

from reapy_boost.tools.network import Server


def run_main_loop() -> None:
    # Get new connections
    SERVER.accept()
    # Process API call requests
    requests = SERVER.get_requests()
    results = SERVER.process_requests(requests)
    SERVER.send_results(results)
    # Run main_loop again
    reapy_boost.defer(run_main_loop)


def get_new_reapy_server() -> Server:
    server_port = reapy_boost.config.REAPY_SERVER_PORT
    reapy_boost.set_ext_state("reapy_boost", "server_port", str(server_port))
    server = Server(server_port)
    return server


if __name__ == "__main__":
    SERVER = get_new_reapy_server()
    run_main_loop()
    reapy_boost.at_exit(
        reapy_boost.delete_ext_state, "reapy_boost", "server_port"
    )
