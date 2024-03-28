#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the value of
the variable X-Request-Id in the response header.
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
