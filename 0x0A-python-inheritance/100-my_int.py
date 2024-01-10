#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int.
"""

class MyInt(int):
    """
    A class MyInt that inherits from int and has the == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Method to invert the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Method to invert the != operator.
        """
        return super().__eq__(other)
