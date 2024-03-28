#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve the given challenge
"""
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) != 3:
        print("Usage: ./script.py <username> <repository>")
        exit(1)
    
    username = argv[1]
    repository = argv[2]
    
    url = f"https://api.github.com/repos/{username}/{repository}/commits?per_page=10"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        commits = response.json()
        
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"SHA: {sha} | Author: {author_name}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)
