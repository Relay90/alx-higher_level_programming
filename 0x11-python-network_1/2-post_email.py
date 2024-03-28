#!/usr/bin/python3
"""
A script that takes in a URL and an email,
Sends a POST request to the passed URL with the email as a parameter,
And displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
