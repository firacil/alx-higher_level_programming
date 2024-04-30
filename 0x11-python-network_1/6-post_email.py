#!/usr/bin/python3
"""
    script that fetches url using requests package
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = (argv[1])
    email = (argv[2])

    # prepare the POST data
    data = {'email': email}

    # send a POST request to the passed URL with the email as parameter
    r = requests.post(url, data=data)
    # Now Let Print it
    print("{}".format(response.text))
