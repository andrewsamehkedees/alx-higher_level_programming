#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """This is a class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """this is the constractor
        Args:
            size: the default value
        Raises:
            TypeError: the type of the input
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) for n in value) or \
           not all(n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

