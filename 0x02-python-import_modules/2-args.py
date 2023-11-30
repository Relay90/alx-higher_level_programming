#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}.", end="\n" if num_args == 0 else ":", sep="")

    for i, arg in enumerate(args, start=1):
        print(f"{'' if num_args == 0 else f'\n{i}: {arg}'}")
