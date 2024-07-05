#!/usr/bin/env python3
'''type-annotated function to_str
'''


def to_str(n: float) -> str:
    '''Cast a floting type number in to a string.
    '''
    return str(n)


if __name__ == '__main__':
    print(f'to_str(3.142)')
    print(to_str(0.00))

    print(to_str.__annotations__)
