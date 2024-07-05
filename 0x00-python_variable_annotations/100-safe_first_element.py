#!/usr/bin/env python3
'''Augment the below code.
'''

from typing import List, Optional, TypeVar


T = TypeVar('T')

def safe_first_element(lst: List[T]) -> Optional[T]:
    '''Augument code with correct duck-typed annotations
    '''
    if lst:
        return lst[0]
    else:
        return None
