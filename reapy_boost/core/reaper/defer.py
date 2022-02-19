"""Define reapy_boost.defer and reapy_boost.at_exit."""

import reapy_boost

import os
import sys
import tempfile
import typing as ty


class Deferrer:
    """Class to register and run deferred calls."""

    _next_call_id: int = 0
    _callbacks: ty.Dict[int, ty.Callable[..., ty.Any]] = {}
    _args: ty.Dict[int, ty.Tuple[ty.Any, ...]] = {}
    _kwargs: ty.Dict[int, ty.Dict[str, ty.Any]] = {}

    def _get_new_call_id(self) -> int:
        new_id = self._next_call_id
        Deferrer._next_call_id += 1
        return new_id

    def _wrapped_open(self, *args: ty.Any,
                      **kwargs: ty.Any) -> ty.Union['ReaperConsole', ty.Any]:
        if args[0] == os.path.join(tempfile.gettempdir(), "reascripterr.txt"):
            return ReaperConsole()
        return open(*args, **kwargs)

    def defer(
        self,
        callback: ty.Callable[..., ty.Any],
        args: ty.Tuple[ty.Any, ...],
        kwargs: ty.Dict[str, ty.Any],
        at_exit: bool = False
    ) -> None:
        call_id = self._get_new_call_id()
        Deferrer._callbacks[call_id] = callback
        Deferrer._args[call_id] = args
        Deferrer._kwargs[call_id] = kwargs
        code = "import sys; sys.modules[{}].Deferrer().run({})".format(
            repr(__name__), call_id
        )
        sys.modules["__main__"].open = self._wrapped_open
        if at_exit:
            sys.modules["__main__"].RPR_atexit(code)
        else:
            sys.modules["__main__"].RPR_defer(code)

    def run(self, call_id: int) -> None:
        # Get callback and run it
        callback = self._callbacks[call_id]
        args = self._args[call_id]
        kwargs = self._kwargs[call_id]
        callback(*args, **kwargs)
        # Clean up
        sys.modules["__main__"].open = open
        for x in Deferrer._callbacks, Deferrer._args, Deferrer._kwargs:
            del x[call_id]


class ReaperConsole:
    """File-like wrapper around the Reaper Console."""

    def close(self) -> None:
        ...

    def flush(self) -> None:
        ...

    def write(self, *args: ty.Any, **kwargs: ty.Any) -> None:
        reapy_boost.print(*args, **kwargs)


def at_exit(
    f: ty.Callable[..., ty.Any], *args: ty.Any, **kwargs: ty.Any
) -> None:
    """
    Make REAPER call a function after script execution.

    The function is also called if excution is terminated by user.

    Parameters
    ----------
    f : callable
        Function to be called later.
    args : tuple, optional
        Positional arguments to pass to ``f``.
    kwargs : dict, optional
        Keyword arguments to pass to ``f``.

    Raises
    ------
    AssertionError
        When called from outside REAPER.

    Examples
    --------
    Typical use case of ``at_exit`` is cleaning up after a ``defer``
    loop.

    The following example opens a file and starts a loop that
    indefinitely writes integers to that file. Since we want the file
    to be closed when the user terminates script execution, call to
    its ``close`` method is deferred to ``reapy_boost.at_exit``.

    >>> import reapy_boost
    >>> file = open("somefile.txt", "w")
    >>> def stupid_loop(i):
    ...     file.write(i)
    ...     reapy_boost.defer(stupid_loop, i + 1)
    ...
    >>> reapy_boost.at_exit(file.close)
    >>> stupid_loop(0)
    """
    message = "reapy_boost.at_exit can only be called inside REAPER."
    assert reapy_boost.is_inside_reaper(), message
    Deferrer().defer(f, args, kwargs, at_exit=True)


def defer(
    f: ty.Callable[..., ty.Any], *args: ty.Any, **kwargs: ty.Any
) -> None:
    """
    Make REAPER call a function later.

    Parameters
    ----------
    f : callable
        Function to be called later.
    args : tuple, optional
        Positional arguments to pass to ``f``.
    kwargs : dict, optional
        Keyword arguments to pass to ``f``.

    Raises
    ------
    AssertionError
        When called from outside REAPER.

    Notes
    -----
    The average time before a defered call is actually run is about
    0.03 seconds (around 30 defered calls are allowed per second).

    Examples
    --------
    Typical use case of ``defer`` is running loops that don't block
    REAPER GUI.

    The following example creates a loop that indefinitely prints
    integers to the REAPER console, without blocking REAPER GUI.

    >>> import reapy_boost
    >>> def stupid_loop(i):
    ...     reapy_boost.print(i)
    ...     reapy_boost.defer(stupid_loop, i + 1)
    ...
    >>> stupid_loop(0)
    """
    # Check we are inside REAPER
    message = "reapy_boost.defer can only be called inside REAPER."
    assert reapy_boost.is_inside_reaper(), message
    Deferrer().defer(f, args, kwargs)
