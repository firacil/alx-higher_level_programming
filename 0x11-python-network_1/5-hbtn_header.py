#!/usr/bin/python3
"""
    script that fetches url using requests package
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = (argv[1])
    r = requests.get(url)
    headers = r.headers
    # Now Let Print it
    print("{}".format(headers.get('X-Request-Id')))
