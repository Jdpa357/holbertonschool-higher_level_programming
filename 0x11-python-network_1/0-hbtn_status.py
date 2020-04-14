#!/usr/bin/python3
"""
Script that fetches holberton intranet status using urllib
"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as hbtn:
        stat = hbtn.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(stat), stat, stat.decode('utf-8')))
