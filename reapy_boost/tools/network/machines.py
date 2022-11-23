import importlib
import sys
import warnings
from ipaddress import IPv4Address
import typing as ty

import reapy_boost
import reapy_boost.config
from reapy_boost import errors
from . import client, web_interface
from .client import LOCALHOST

_CLIENTS_TYPE = ty.Dict['Host', client.Client]

CLIENT: ty.Optional[client.Client] = None
CLIENTS: ty.Optional[_CLIENTS_TYPE] = None


class Host:

    def __init__(
        self,
        host: IPv4Address,
        port: int = reapy_boost.config.WEB_INTERFACE_PORT,
    ):
        self.port, self.host = port, host

    def __eq__(self, other):
        if not isinstance(other, Host):
            return False
        return self.port, self.host == other.port, other.host

    def __hash__(self) -> int:
        return self.host.__hash__() + self.port


def get_selected_client():
    return CLIENT


def get_selected_machine_host():
    """Return host of the currently selected machine.

    Returns
    -------
    host : str or None
        None is returned when running from inside REAPER and
        no slave machine is selected.
    """
    return None if CLIENT is None else CLIENT.host


def reconnect():
    """
    Reconnect to REAPER ReaScript API.

    Examples
    --------
    Assume no REAPER instance is active.
    >>> import reapy_boost
    errors.DisabledDistAPIWarning: Can't reach distant API. Please start REAPER, or
    call reapy_boost.config.enable_dist_api() from inside REAPER to enable distant
    API.
      warnings.warn(errors.DisabledDistAPIWarning())
    >>> p = reapy_boost.Project()  # Results in error
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "reapy_boost\\core\\project\\project.py", line 26, in __init__
        id = RPR.EnumProjects(index, None, 0)[0]
    AttributeError: module 'reapy_boost.reascript_api' has no attribute 'EnumProjects'
    >>> # Now start REAPER
    ...
    >>> reapy_boost.reconnect()
    >>> p = reapy_boost.Project()  # No error!
    """
    if not reapy_boost.is_inside_reaper():
        host = get_selected_machine_host()
        if host is None:
            # We are outside REAPER, so this means initial import failed to
            # connect and we want to retry with default host (i.e. localhost)
            host = LOCALHOST
        try:
            del CLIENTS[host]
        except KeyError:
            pass
        connect(host)


class connect:
    """Connect to slave machine.

    reapy_boost instructions will now be run on the selected machine.
    If used as a context manager, the slave machine will only be
    selected in the corresponding context.

    Parameters
    ----------
    host : str, optionalal
        Slave machine host. If None, selects default ``reapy_boost``
        behavior (i.e. local REAPER instance).

    See also
    --------
    ``connect_to_default_machine``
        Connect to default slave machine (i.e. local REAPER instance).
    """

    def __init__(self, host: ty.Optional[Host]):
        global CLIENT
        self.previous_client = CLIENT
        global CLIENTS
        CLIENTS = CLIENTS or {}
        try:
            host = host or Host(IPv4Address(LOCALHOST))
            if host not in CLIENTS:
                register_machine(host)
            CLIENT = CLIENTS[host]
            if hasattr(reapy_boost,
                       'reascript_api'):  # False during initial import
                importlib.reload(reapy_boost.reascript_api)
        except errors.DisabledDistAPIError as e:
            if host and host != Host(IPv4Address(LOCALHOST)):
                raise e
            warnings.warn(errors.DisabledDistAPIWarning())

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        global CLIENT
        CLIENT = self.previous_client
        importlib.reload(reapy_boost.reascript_api)


class connect_to_default_machine(connect):
    """Select default slave machine (i.e. local REAPER instance)."""

    def __init__(self):
        super().__init__()


def register_machine(host: Host):
    """Register a slave machine.

    Parameters
    ----------
    host : str
        Slave machine host (e.g. ``LOCALHOST``).

    See also
    --------
    ``reapy_boost.connect``
    """
    if reapy_boost.is_inside_reaper() and host == LOCALHOST:
        msg = "A REAPER instance can not connect to istelf."
        raise errors.InsideREAPERError(msg)
    if isinstance(host, str):
        # for the case someone still uses string address.
        host = Host(IPv4Address(host))
    interface_port = host.port
    interface = web_interface.WebInterface(interface_port, str(host.host))
    global CLIENTS
    CLIENTS = CLIENTS or {}
    CLIENTS[host] = client.Client(interface.get_reapy_server_port(), host.host)


if not reapy_boost.is_inside_reaper():
    assert Host(IPv4Address(LOCALHOST)) == Host(IPv4Address(LOCALHOST))
    host = Host(IPv4Address(LOCALHOST))
    connect(host)
    # CLIENTS = CLIENTS or {}
    # CLIENTS[host] = CLIENT
