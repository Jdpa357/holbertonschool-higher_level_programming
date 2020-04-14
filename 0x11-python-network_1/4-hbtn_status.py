#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
displays the body of the response in a special format
"""
import requests

if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(r.text), r.text))
