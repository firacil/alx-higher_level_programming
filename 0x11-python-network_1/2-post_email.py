#!/usr/bin/python3
"""
    script that send http request and
    display X-Request-Id found in header of response
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    # prepare post data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # create a post request
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("{}".format(body.decode('utf-8')))
