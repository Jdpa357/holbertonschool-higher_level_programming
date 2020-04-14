#!/usr/bin/pytho3
"""
Script that takes in a URL, sends a request and displays the X-request-id value
of the variable found in the header of the response
"""
import urllib.request
import sys

if __name__ = '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))
