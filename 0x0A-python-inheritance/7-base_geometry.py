#!/usr/bin/python3
"""
This module contains a class BaseGeometry with a public instance method area and integer_validator.
"""

class BaseGeometry:
    """
    A class BaseGeometry with a public instance method area and integer_validator.
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value.

        Args:
            name: Always a string.
            value: Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
