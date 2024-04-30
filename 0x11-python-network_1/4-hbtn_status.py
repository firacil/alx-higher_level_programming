#!/usr/bin/python3
"""
    script that fetches url using requests package
"""
import requests


if __name__ == "__main__":

    url = ('https://alx-intranet.hbtn.io/status')
    r = requests.get(url)
    print('Body response:')
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format((r.text)))
