#!/usr/bin/env python3
'''adds type annotations to the function.
'''
from typing import Dict, TypeVar, Optional


K = TypeVar('K')
V = TypeVar('V')

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    '''Given the parameters and the return values.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
