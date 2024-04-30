#!/usr/bin/python3
"""
    script that fetchs http request
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print('Body response:')
print(f'    - type: {type(content)}')
print(f'    - content: {content}')
print(f'    - utf8 content: {utf8_content}')
