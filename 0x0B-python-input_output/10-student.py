#!/usr/bin/python3
class Student:
    """
    Defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiate a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student.

        If attrs is a list of strings, retrieve attribute names contained in this list only.
        Otherwise, retrieve all attributes.

        Args:
            attrs (list): A list of strings representing attribute names to retrieve.
        Returns:
            dict: A dictionary representation of the Student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
