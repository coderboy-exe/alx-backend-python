#!/usr/bin/env python3
""" Returns the first element of a list """

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ function definition """
    if lst:
        return lst[0]
    else:
        return None
