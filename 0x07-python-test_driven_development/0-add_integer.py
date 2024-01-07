#!/usr/bin/python3
"""
Function
"""
def add_integer(a, b=98):
    """
    Function to add two numbers

    Parameters:
    a (int, float): The first parameter.
    b (int, float): The second parameter.

    Returns:
    int: The return value. a + b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
