#!/usr/bin/python3
"""
This module contains a function
"""

def inherits_from(obj, a_class):
    """
    check instance of the class

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True or False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
