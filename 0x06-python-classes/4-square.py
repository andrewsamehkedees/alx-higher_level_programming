#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """This is a class that defines a square.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):
        """this is the constractor
        Args:
            size: the default valeo is 0
        Raises:
            TypeError: the type of the input
            ValueError: the value of the input
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """class area
        Return: the square of the size 
        """
        return self.__size * self.__size

