#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Instantiation with size.

        Args:
            size: Size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Method that returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Method that returns the square description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
