#!/usr/bin/python3
"""
    script that takes in a URL, sends a
    request to the URL and displays the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":

    try:
        url = argv[1]
        r = requests.get(url)
        print(r.text)

    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(r.status_code))
