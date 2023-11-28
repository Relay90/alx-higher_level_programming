#!/usr/bin/python3
import random

# Do not modify the following line
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10  # Using abs() to handle negative numbers
if number < 0;
digit = -digit
# Check conditions and print the result
print(f"Last digit of {number} is {last_digit}", end=' ')
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
