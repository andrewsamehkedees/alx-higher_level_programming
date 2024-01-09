#!/usr/bin/python3
"""this is the append wrtie function"""


def append_write(filename="", text=""):
    """
    Append a string to a UTF8 text file and return the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
