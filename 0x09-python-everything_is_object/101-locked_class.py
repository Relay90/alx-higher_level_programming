#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except AttributeError as e:
    print("[{}] {}".format(e.__class__.__name__, e))
