# Homecooked

Author: [roerohan](https://github.com/roerohan)

All you have to do is optimize the code you already got.

# Requirements

- Python

# Source

```
I cannot get this to decrypt!

Download the file below.

[decrypt.py](https://ctf.nahamcon.com/files/6997fd70f4c38f9efcc4984193bcd541/decrypt.py?token=eyJ1c2VyX2lkIjoyMzk2LCJ0ZWFtX2lkIjpudWxsLCJmaWxlX2lkIjoyfQ.XuYscg.X77rndeap6B6BGNQQulUqJbzLEE)
```

```python
# decrypt.py

import base64
num = 0
count = 0
cipher_b64 = b"MTAwLDExMSwxMDAsOTYsMTEyLDIxLDIwOSwxNjYsMjE2LDE0MCwzMzAsMzE4LDMyMSw3MDIyMSw3MDQxNCw3MDU0NCw3MTQxNCw3MTgxMCw3MjIxMSw3MjgyNyw3MzAwMCw3MzMxOSw3MzcyMiw3NDA4OCw3NDY0Myw3NTU0MiwxMDAyOTAzLDEwMDgwOTQsMTAyMjA4OSwxMDI4MTA0LDEwMzUzMzcsMTA0MzQ0OCwxMDU1NTg3LDEwNjI1NDEsMTA2NTcxNSwxMDc0NzQ5LDEwODI4NDQsMTA4NTY5NiwxMDkyOTY2LDEwOTQwMDA="

def a(num):
    if (num > 1):
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        return True
    else:
        return False
       
def b(num):
    my_str = str(num)
    rev_str = reversed(my_str)
    if list(my_str) == list(rev_str):
       return True
    else:
       return False


cipher = base64.b64decode(cipher_b64).decode().split(",")

while(count < len(cipher)):
    if (a(num)):
        if (b(num)):
            print(chr(int(cipher[count]) ^ num), end='', flush=True)
            count += 1
            if (count == 13):
                num = 50000
            if (count == 26):
                num = 500000
    else:
        pass
    num+=1

print()
```

- [decrypt.py](./decrypt.py)

# Exploitation

As you see in the source, there are 2 functions, `a()` and `b()`. When you run the code you got from the site, you see the starting of the flag is printed automatically: `flag{pR1m3s_4re_co0ler_Wh3`. Now, it takes a while to print the rest of the flag. Well, a long time XD. So it's best if you optimize the `a()` function a little bit.

```python
import base64
num = 0
count = 0
cipher_b64 = b"MTAwLDExMSwxMDAsOTYsMTEyLDIxLDIwOSwxNjYsMjE2LDE0MCwzMzAsMzE4LDMyMSw3MDIyMSw3MDQxNCw3MDU0NCw3MTQxNCw3MTgxMCw3MjIxMSw3MjgyNyw3MzAwMCw3MzMxOSw3MzcyMiw3NDA4OCw3NDY0Myw3NTU0MiwxMDAyOTAzLDEwMDgwOTQsMTAyMjA4OSwxMDI4MTA0LDEwMzUzMzcsMTA0MzQ0OCwxMDU1NTg3LDEwNjI1NDEsMTA2NTcxNSwxMDc0NzQ5LDEwODI4NDQsMTA4NTY5NiwxMDkyOTY2LDEwOTQwMDA="

pl = {}

p = open('primes1.txt').read().split()
for i in p:
    pl[int(i)] = True

def a(num):
    if (num > 1):
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        return True
    else:
        return False

def primes(num):
    return num in pl
       
def b(num):
    my_str = str(num)
    rev_str = my_str[::-1]
    if my_str == rev_str:
       return True
    else:
       return False


cipher = base64.b64decode(cipher_b64).decode().split(",")

while(count < len(cipher)):
    if (primes(num)):
        if (b(num)):
            print(chr(int(cipher[count]) ^ num), end='', flush=True)
            count += 1
            if (count == 13):
                num = 50000
            if (count == 26):
                num = 500000
    else:
        pass
    num+=1

print()
```

So, we create a new function `primes()`, which can now replace `a()`. All it does is basically, read the first million primes from a file called [`primes1.txt`](./primes1.txt). Now, create a python dictionary of primes and check if the parameter is in that dictionary. This prints out the flag: `flag{pR1m3s_4re_co0ler_Wh3n_pal1nDr0miC}`.