#!/usr/bin/python3

def uppercase(string):
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            print("{}".format(uppercase_char), end='')
        else:
            print("{}".format(char), end='')
    print()

