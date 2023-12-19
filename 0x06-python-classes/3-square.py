#!/usr/bin/python3
"""define class square"""

class Square:
    """this is the constractor
    Args:
        size: the default valeo is 0
    Raises:
        TypeError: the type of the input
    ValueError: the value of the input
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """class area"""

    def area(self):
        return self.__size * self.__size

