#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text_list = [letter + "\n\n" if letter in ".?:"
                     else letter for letter in text]
    print("".join(character for character in new_text_list), end='')
