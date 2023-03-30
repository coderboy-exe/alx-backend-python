#/usr/bin/env python3
""" Returns the first element of a list """

from typing import Union, Any, Sequence, Mapping, TypeVar


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
