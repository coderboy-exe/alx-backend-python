#!/usr/bin/env python3
""" Returns the first element of a list """

from typing import Union, Any, Sequence, Mapping, TypeVar


T = TypeVar('T')
Def = Union[T, None]
Ret = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Ret:
    """function def"""
    if key in dct:
        return dct[key]
    else:
        return default
