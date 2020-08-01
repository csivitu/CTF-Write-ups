# Prophecy

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Python
- Pwntools (Linux)

# Source

```
C A N Y O U S E E T H E F U T U R E ?

Connect with:
nc jh2i.com 50012
```

# Exploitation

Everytime you connect using netcat, it makes you guess the number, and if you guess incorrectly, it tells you what the number was. Now, when you guess incorrectly, you know the number. Connect recursively and you get all the numbers.


```python
from pwn import remote

numbers = [0] * 100

i = 0

while True:
    if i == 0:
        r = remote("jh2i.com", 50012)

    try:
        re = r.recvuntil(">")
    except Exception as e:
        r.interactive()
        continue

    print(re.decode(), end=" ")

    r.sendline(str(numbers[i]).encode())
    print(str(numbers[i]))

    print([i for i in numbers if i != 0])

    if numbers[i] == 0:
        res = r.recvuntil(".").decode()
        res += r.recv(1024).decode()
        numbers[i] = res.split("W A S ")[1].strip()
        i = 0
    else:
        i += 1
```

The scripts runs for a few minutes and in the end it gives you the flag.

```bash
$ python script.py
...

 W H A T I S T H E N E X T N U M B E R T O C O M E F R O M T H E F U T U R E ?

> 83643
['99126', '76106', '32378', '49560', '87935', '17366', '36639', '33561', '51241', '24009', '82718', '65774', '87030', '53097', '53885', '29931', '10890', '20583', '46190', '83643']
[*] Switching to interactive mode
 ==============================================================================
 
                       Y O U T O O C A N S E E T H E F U T U R E 
==============================================================================
flag{does_this_count_as_artificial_intelligence}
```

The flag is

```
flag{does_this_count_as_artificial_intelligence}
```
