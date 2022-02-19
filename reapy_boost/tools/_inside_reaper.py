import contextlib
import functools
import typing as ty

import reapy_boost
import reapy_boost.config
from .network import machines
# if not reapy_boost.is_inside_reaper():
#     try:
#         from .network import Client, WebInterface
#         _WEB_INTERFACE = WebInterface(reapy_boost.config.WEB_INTERFACE_PORT)
#         _CLIENT = Client(_WEB_INTERFACE.get_reapy_server_port())
#     except DisabledDistAPIError:
#         import warnings
#         warnings.warn(DisabledDistAPIWarning())
#         _CLIENT = None

# from typing import Callable, Concatenate, TypeVar

FuncType = ty.Callable[..., ty.Any]
F = ty.TypeVar('F', bound=ty.Union[FuncType, property])


def dist_api_is_enabled() -> bool:
    """Return whether reapy_boost can reach REAPER from the outside."""
    return machines.get_selected_client() is not None


class inside_reaper(contextlib.ContextDecorator):
    """
    Context manager for efficient calls from outside REAPER.

    It can also be used as a function decorator.

    Examples
    --------
    Instead of running:

    >>> project = reapy_boost.Project()
    >>> l = [project.bpm for i in range(1000)

    which takes around 30 seconds, run:

    >>> project = reapy_boost.Project()
    >>> with reapy_boost.inside_reaper():
    ...     l = [project.bpm for i in range(1000)
    ...

    which takes 0.1 seconds!

    Example usage as decorator:

    >>> @reapy_boost.inside_reaper()
    ... def add_n_tracks(n):
    ...     for x in range(n):
    ...         reapy_boost.Project().add_track()

    """

    def __call__(
        self,
        func: F,
        encoded_func: ty.Optional[ty.Dict[str, object]] = None
    ) -> F:
        if reapy_boost.is_inside_reaper():
            return func
        if isinstance(func, property):
            return DistProperty.from_property(func)
        # Check if the decorated function is from reapy_boost
        module_name = func.__module__
        if module_name == 'reapy_boost' or module_name.startswith(
            'reapy_boost.'
        ):

            @functools.wraps(func)
            def wrap(*args, **kwargs):
                f = func if encoded_func is None else encoded_func
                client = machines.get_selected_client()
                return client.request(f, {"args": args, "kwargs": kwargs})

            return wrap
        # Otherwise, use the context manager
        return super().__call__(func)

    def __enter__(self) -> None:
        if not reapy_boost.is_inside_reaper():
            machines.get_selected_client().request("HOLD")

    def __exit__(self, exc_type, exc_val, exc_tb):  # type: ignore
        if not reapy_boost.is_inside_reaper():
            machines.get_selected_client().request("RELEASE")
        return False


class DistProperty(property):

    _inside_reaper = inside_reaper()

    @classmethod
    def from_property(cls, p: property) -> property:
        return cls().getter(p.fget).setter(p.fset).deleter(p.fdel)

    @staticmethod
    def _encode(f: F, method_name: str) -> ty.Dict[str, object]:
        return {
            "__callable__": True,
            "module_name": f.__module__,
            "name": "{}.f{}".format(f.__qualname__, method_name)
        }

    def getter(self, fget: F) -> property:
        if fget is not None:
            fget = self._inside_reaper(fget, self._encode(fget, "get"))
        return super().getter(fget)

    def setter(self, fset: F) -> property:
        if fset is not None:
            fset = self._inside_reaper(fset, self._encode(fset, "set"))
        return super().setter(fset)

    def deleter(self, fdel: F) -> property:
        if fdel is not None:
            fdel = self._inside_reaper(fdel, self._encode(fdel, "del"))
        return super().deleter(fdel)
