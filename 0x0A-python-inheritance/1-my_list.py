#!/usr/bin/python3
"""
the module
"""


class MyList(list):
    """
    A class that inherits from list.

    Methods:
        print_sorted: Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
