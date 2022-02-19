"""Encode and decode ``reapy_boost`` objects as JSON."""

import importlib
import inspect
import json
import operator
import sys
import typing as ty
import types
if ty.TYPE_CHECKING:
    import reapy_boost

T1 = ty.TypeVar('T1')


class ClassCache(ty.Dict[str, T1]):

    _core: ty.Optional[types.ModuleType] = None

    def __missing__(self, key: str) -> T1:
        if self._core is None:
            # The import is here because otherwise there is an import loop
            # and to perform import just once.
            self._core = importlib.import_module("reapy_boost.core")
        self[key] = getattr(self._core, key)
        return self[key]


_CLASS_CACHE: ClassCache[ty.Type['reapy_boost.ReapyObject']] = ClassCache()


class ReapyEncoder(json.JSONEncoder):

    def default(self, x: ty.Any) -> ty.Any:
        if hasattr(x, '_to_dict'):
            return x._to_dict()
        elif inspect.ismethod(x):
            return {"__self__": x.__self__, "__method_name__": x.__name__}
        elif callable(x):
            return {
                "__callable__": True,
                "module_name": x.__module__,
                "name": x.__qualname__
            }
        elif isinstance(x, slice):
            return {"__slice__": True, "args": (x.start, x.stop, x.step)}
        return json.JSONEncoder.default(self, x)


def loads(s: ty.Union[ty.Text, bytes]) -> ty.Any:
    return json.loads(s, object_hook=object_hook)


def dumps(x: ty.Any) -> str:
    return json.dumps(x, cls=ReapyEncoder)


def object_hook(x: ty.Any) -> ty.Any:
    if "__reapy__" in x:
        reapy_class = _CLASS_CACHE[x["class"]]
        return reapy_class(*x["args"], **x["kwargs"])
    elif "__method_name__" in x:
        return getattr(x["__self__"], x["__method_name__"])
    elif "__callable__" in x:
        module_name, name = x["module_name"], x["name"]
        try:
            module = sys.modules[module_name]
        except KeyError:
            module = importlib.import_module(module_name)
        return operator.attrgetter(name)(sys.modules[module_name])
    elif "__slice__" in x:
        return slice(*x["args"])
    else:
        return x
