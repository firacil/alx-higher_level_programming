#!/usr/bin/python3
"""

module contain function that indent texts

"""


def text_indentation(text):
    ''' function prints a text with 2 new lines after each ".", ":" or "?"

        Args:
            text (str): string to be printed

        Raises:
            TypeError: if text is not string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
