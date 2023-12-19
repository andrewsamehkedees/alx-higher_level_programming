#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """This is a class that defines a square.
    """

    def __init__(self, size=0):
        """this is the constractor
        Args:
            size: the default valeo is 0
        Raises:
            TypeError: the type of the input
            ValueError: the value of the input
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
