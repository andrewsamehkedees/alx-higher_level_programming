#!/usr/bin/python3
class Square:
    """This is a class that defines a square.
    It is used to control the size attribute in a square object.
    """
    def __init__(self, size):
        """Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size
