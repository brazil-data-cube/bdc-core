#
# This file is part of BDC Core.
# Copyright (C) 2019-2020 INPE.
#
# BDC Core is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

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
