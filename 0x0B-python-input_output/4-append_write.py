Learn more or give us feedback
#!/usr/bin/python3

"""
append_write module.
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, 'a') as f:
        c = f.write(text)
    return c
