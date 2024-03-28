#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests

def main():
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Success! Connection established.")
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    else:
        print(f"Error: Failed to fetch URL. Status code: {response.status_code}")

if __name__ == '__main__':
    main()
