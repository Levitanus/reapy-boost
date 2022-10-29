from typing import Any, Dict, Iterator, Tuple, Type, TypedDict
import reapy_boost
import reapy_boost.reascript_api as RPR

ReapyObjectDict = TypedDict(
    'ReapyObjectDict', {
        "__reapy__": bool,
        "class": str,
        "args": Tuple[Any, ...],
        "kwargs": Dict[str, Any]
    }
)


class ReapyMetaclass(type):

    @property
    def _reapy_parent(self) -> Type['ReapyObject']:
        """Return first reapy_boost parent class."""
        for candidate in self.__mro__:
            if candidate.__module__.startswith('reapy_boost.'):
                return candidate
        raise TypeError(f'cannot find reapy_boost class in {self.__mro__}')


class ReapyObject(metaclass=ReapyMetaclass):
    """Base class for reapy_boost objects."""
    id: str

    def __eq__(self, other: object) -> bool:
        return repr(self) == repr(other)

    def __repr__(self) -> str:

        def to_str(x):
            if isinstance(x, str):
                return "\"{}\"".format(x)
            return str(x)

        args = ", ".join(map(to_str, self._args))
        kwargs = ", ".join(
            ("{}={}".format(k, to_str(v)) for k, v in self._kwargs.items())
        )
        if args and kwargs:
            brackets = ", ".join((args, kwargs))
        else:
            brackets = args if args else kwargs
        rep = "{}({})".format(self.__class__.__name__, brackets)
        return rep

    @property
    def _args(self) -> Tuple[()]:
        return ()

    def _get_pointer_and_name(self) -> Tuple[int, str]:
        name, pointer = self.id.split(')')
        return int(pointer, base=16), name[1:]

    @property
    def _is_defined(self) -> bool:
        if hasattr(self, "id"):
            return not self.id.endswith("0x0000000000000000")
        raise NotImplementedError

    @property
    def _kwargs(self) -> Dict[str, object]:
        return {}

    def _to_dict(self) -> ReapyObjectDict:
        return {
            "__reapy__": True,
            "class": self.__class__._reapy_parent.__name__,
            "args": self._args,
            "kwargs": self._kwargs
        }


class ReapyObjectList(ReapyObject):
    """Abstract class for list of ReapyObjects."""

    def __iter__(self) -> Iterator[ReapyObject]:
        for i in range(len(self)):
            yield self[i]
