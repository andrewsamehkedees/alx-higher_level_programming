#!/usr/bin/python3
def lookup(obj):
    """
    Function to get a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the names of the object's attributes and methods.
    """
    return dir(obj)
