from typing import List
import reapy_boost
from reapy_boost.tools import json

import os
import sys


@reapy_boost.inside_reaper()
def _get_api_names() -> List[str]:
    return __all__


if reapy_boost.is_inside_reaper():
    # Import functions without the useless starting "RPR_".
    import reaper_python as _RPR
    __all__ = [s[4:] for s in _RPR.__dict__ if s.startswith("RPR_")]
    for s in __all__:
        exec("{} = _RPR.__dict__['{}']".format(s, "RPR_" + s))

    from reapy_boost import additional_api as _A_API
    for s in _A_API.__dict__:
        exec("from reapy_boost.additional_api import {}".format(s))

    # Import SWS functions.
    try:
        sys.path.append(os.path.join(_RPR.RPR_GetResourcePath(), 'Scripts'))
        import sws_python as _SWS
        sws_functions = set(_SWS.__dict__) - set(_RPR.__dict__)
        __all__ += list(sws_functions)
        for s in sws_functions:
            exec("from sws_python import {}".format(s))
    except ImportError:  # SWS is not installed
        pass
else:
    if reapy_boost.dist_api_is_enabled():
        __all__ = _get_api_names()
        func_def = (
            "@reapy_boost.inside_reaper()\n"
            "def {name}(*args): return (name)(*args)"
        )
        exec("\n".join(func_def.format(name=name) for name in __all__))
        del func_def
