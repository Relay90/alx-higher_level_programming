#!/usr/bin/python3
if __name__ == "__main__":
a = 10
b = 5

with open('calculator_1.py', 'r') as file:
    code = file.read()

# Execute the content of the file
exec(code)

add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)

# Print the results
print(f"{a} + {b} = {add_result}")
print(f"{a} - {b} = {sub_result}")
print(f"{a} * {b} = {mul_result}")
print(f"{a} / {b} = {div_result}")
