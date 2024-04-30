#!/usr/bin/python3
"""
    script that send http request and
    display body response and handle errors
"""
import urllib.request
import urllib.parse
from sys import argv
import urllib.error


if __name__ == "__main__":
    url = argv[1]

    # create a post request
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("{}".format(body.decode('utf-8')))

    except urllib.error.HTTPError as e:
        # handle different HTTP error codes
        print("Error code: {}".format(e.code))
