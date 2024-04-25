#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s "$1" | grep -o -m 1 'HTTP/1.1 200 OK' && curl -s "$1"
