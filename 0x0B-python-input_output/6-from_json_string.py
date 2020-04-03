#!/usr/bin/python3

"""
from_json_to_string
"""

import json


def from_json_string(my_str):
    """Return an object (Python data structure) represented
    by a JSON string"""
    return json.loads(my_str)
