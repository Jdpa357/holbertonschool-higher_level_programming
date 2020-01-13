#!/usr/bin/python3
"""
text indentation Module
Function that prints a text with a special format
"""


def text_indentation(text):
    """This function prints a text with 2 new lines
    after each of these characters: . or ? or :
    """
    if not isinstance(text, str):
         raise TypeError('text must be a string')
    text = text.replace('. ', '.') \
               .replace('.', '.\n\n') \
               .replace(', ', ',') \
               .replace(',', ',\n\n') \
               .replace('? ', '?') \
               .replace('?', '?\n\n') \
               .replace(': ', ':') \
               .replace(':', ':\n\n')
    paragraph = text.splitlines(keepends=True)
    outputtext = ''
    for i in paragraph:
        outputtext += i.strip(' ')
    print(outputtext, end='')
