#!/usr/bin/python3
a = 1
b = 2

with open('add_0.py', 'r') as file:
    code = file.read()
result = add(a, b)
print("{} + {} = {}".format(a, b, result))
