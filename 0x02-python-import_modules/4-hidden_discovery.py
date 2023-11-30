#!/usr/bin/python3
import dis

def print_hidden_names():
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()

    # Disassemble the bytecode
    instructions = dis.get_instructions(code)

    # Extract names that don't start with '__'
    names = {i.argval for i in instructions if isinstance(i.argval, str) and not i.argval.startswith('__')}
    
    # Print names in alphabetical order
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_hidden_names()
