#!/usr/bin/python3

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./calculator_1.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    result = None

    if operator == '+':
        result = add(a, b)
        print(f"{a} + {b} = {result}")
    elif operator == '-':
        result = sub(a, b)
        print(f"{a} - {b} = {result}")
    elif operator == '*':
        result = mul(a, b)
        print(f"{a} * {b} = {result}")
    elif operator == '/':
        result = div(a, b)
        print(f"{a} / {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
