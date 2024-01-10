#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method that returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method that returns the rectangle description.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
