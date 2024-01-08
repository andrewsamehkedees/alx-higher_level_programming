#!/usr/bin/python3
def text_indentation(text):
    """
    Function to print a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
    text (str): The text to be printed.

    Returns:
    None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")))
