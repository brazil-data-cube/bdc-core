"""
This file contains the common utilities used through
Brazil Data Cube projects
"""

def replace_by_list(my_string, list_strs, new_value):
    """
    Applies a character override to a string based on a list of strings
    """
    for s in list_strs:
        my_string = my_string.replace(s, new_value)
    return my_string
