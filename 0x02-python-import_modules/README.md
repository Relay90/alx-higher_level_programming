0x02-python-import_modules

0-add.py
........
This code reads the content of the file add_0.py and executes it using exec(). Then, it calls the add() function with the values of a and b assigned previously and prints the result in the desired format

1-calculation.py
................
This code reads the content of the file calculator_1.py and executes it using exec(). Then, it calls each of the imported functions (add, sub, mul, div) with the values of a and b assigned previously and prints the results in the desired format without using more than four print statements.

2-args.py
..........
This script prints the number of arguments initially. If there are no arguments, it ends the line. If there are arguments, it prints a colon and starts a new line, then proceeds to print each argument with its index number.

3-infinite_add.py
.................
This script retrieves all the command-line arguments (sys.argv[1:]), converts them to integers using map(int, args), sums them up using sum(), and finally prints the result.

4-hidden_discovery.py
.....................
This script opens the hidden_4.pyc file in binary mode, disassembles its bytecode using dis.get_instructions, extracts names that don't start with '__' from the instructions, and prints them in alphabetical order.

5-variable_load.py
------------------
This script, when executed, imports the variable a from the variable_load_5.py file and prints its value

100-my_calculator.py
-------------------
This script imports the functions add, sub, mul, and div from calculator_1.py. It checks the number of arguments provided in the command line, performs the operation specified by the operator ('+', '-', '*', '/'), and prints the result accordingly. If there are any issues with the input or operator, it prints the respective error message and exits with a status of 1

101-easy_print.py
-----------------
This code imports the sys module and utilizes sys.stdout.write to output #pythoniscool followed by a newline character, all within two lines.

102-magic_calculation.py
------------------------
This function performs the following steps:
Imports the add and sub functions from the magic_calculation_102 module.
Compares a and b. If a is less than b, it performs an addition operation using add.
If the comparison is false (a is not less than b), it performs a subtraction operation using sub.
Returns the result of the calculation based on the condition.

103-fast_alphabet.py
--------------------
This code utilizes the string module to access the lowercase alphabet (string.ascii_lowercase). It uses translate() with str.maketrans() to remove all lowercase characters, effectively printing the uppercase alphabet without using loops, conditional statements, string literals, or system calls
