#!/usr/bin/python3

def uppercase(string):
    uppercase_str = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            uppercase_str += "{}".format(uppercase_char)
        else:
            uppercase_str += "{}".format(char)
    print(uppercase_str)
