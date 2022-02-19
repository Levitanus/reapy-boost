import functools

from reapy_boost.errors import ExtensionNotFoundError

import reapy_boost

from pathlib import Path
from warnings import warn
import typing as ty
import re

FuncType = ty.Callable[..., ty.Any]
F = ty.TypeVar('F', bound=FuncType)


def depends_on_extension(extension: str, url: str) -> ty.Callable[[F], F]:
    """Return a decorator to indicate dependency to an extension.

    If the extension is not available, an `ExtensionNotFoundError`
    will be raised when calling the decorated function.

    Parameters
    ----------
    extension : str
        Extension name.
    url : str
        URL of the download page or installation instructions of
        the extension.
    """
    message = "module 'reapy_boost.reascript_api' has no attribute"

    def decorator(f: F) -> F:
        """Indicate dependency of a function to an extension.

        If the extension is not available, an `ExtensionNotFoundError`
        will be raised when calling the decorated function.
        """

        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except AttributeError as exc:
                if exc.args[0].startswith(message):
                    raise ExtensionNotFoundError(extension, url)
                else:
                    raise exc

        return wrapped

    return decorator


depends_on_sws = depends_on_extension('SWS', 'www.sws-extension.org')

_preambula = """
import reapy_boost
if reapy_boost.is_inside_reaper():
    from reaper_python import *\n"""
_decorator = """@reapy_boost.inside_reaper()\n"""


def generate_imgui() -> None:
    """Generate API for dear ImGui.

    Note
    ----
    Extension ReaImGui (https://github.com/cfillion/reaimgui)
    has to be installed.
    """
    api_path = Path(
        reapy_boost.get_resource_path()
    ).joinpath("Scripts/ReaTeam Extensions/API/imgui_python.py")
    if not api_path.exists():
        warn(
            "ImGUI API path does not exists." +
            " Install the extension with ReaPack"
        )
        return
    new_path = Path(__file__).parent.parent.joinpath('ImGui.py')
    assert new_path.exists()
    with open(new_path, 'w') as new:
        new.write(_preambula)
        with open(api_path, 'r') as old:
            for line in old.readlines():
                if line.startswith("from reaper_python import *"):
                    continue
                line = re.sub(r'def ImGui_', _decorator + 'def ', line)
                if not re.search(r"rpr_getfp\('ImGui_", line):
                    line = re.sub(r'ImGui_', '', line)
                # newlines.append(line)
                new.write(line)
