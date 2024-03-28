#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == '__main__':
    q = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        response_json = r.json()
        user_id, user_name = response_json.get('id'), response_json.get('name')
        if 'id' in response_json and 'name' in response_json:
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
