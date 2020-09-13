# modulus_operandi

Author: [roerohan](https://github.com/roerohan) and [thebongy](https://github.com/thebongy)

# Requirements

- Python

# Source

```
Can't play CSAW without your favorite block cipher!

nc crypto.chal.csaw.io 5001
```

# Exploitation

The exploit is based on the fact that the ciphertext generated using ECB will have repeating blocks because of the way it works, while CBC will not have such blocks.
<br />

The following script can be used to get the flag.

```py
from pwn import remote

l = []

def connect():
    r = remote('crypto.chal.csaw.io', 5001)

    print(r.recvuntil('\n').decode())

    return r


def send(r, x):
    r.sendline(x)
    print(x)


def run(r):
    x = r.clean()
    print(x)                     # Enter plaintext

    send(r, 'a' * 64)

    print(r.recvuntil('Ciphertext is:  '))
    x = r.recvline().decode()    # Ciphertext value
    print(x)

    if x[0:32] == x[32:64]:
        mode = 'ECB'
        l.append(0)
    else:
        mode = 'CBC'
        l.append(1)

    print(r.recvline())           # ECB or CBC

    send(r, mode)



def solve():
    r = connect()

    i = 0
    while True:
        try:
            run(r)
        except:
            print(i)
            print(r.recvall())
            print(l)
            exit(1)
        i+=1

    r.interactive()

solve()

'''
[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1]
'''
```

In this list, ECB is 0 and CBC is 1. You can then group these into 8 and treat them as binary to get the flag.

```py
>>> ''.join([chr(int(''.join(map(str, l[0+i:8+i])), 2)) for i in range(0, len(l
), 8)])
'flag{ECB_re@lly_sUck$}'
```
