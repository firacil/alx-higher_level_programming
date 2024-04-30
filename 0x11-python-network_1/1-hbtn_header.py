#!/usr/bin/python3
"""
    script that send http request and
    display X-Request-Id found in header of response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = urllib.request.Request(argv[1])
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print("{}".format(headers.get('X-Request-Id')))
