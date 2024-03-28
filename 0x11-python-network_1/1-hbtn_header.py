#!/usr/bin/python3
"""
A script that takes in a URL,
Sends a request to the URL,
And displays the value of the X-Request-Id
variable found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
