#!/usr/bin/python3
"""
    script to list most recent(10) commits on given github repo.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for c in range(10):
            print("{}: {}".format(
                commits[c].get("sha"),
                commits[c].get("commit").get("author").get("name")))
    except IndexError:
        pass
