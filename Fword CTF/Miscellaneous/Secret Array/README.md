# Secret Array

Author: [roerohan](https://github.com/roerohan) and [namsnath](https://github.com/namsnath)

# Requirements

- Python

# Source

- nc secretarray.fword.wtf 1337

# Exploitation

We can get the sum of 2 numbers, 1337 times. We can send out 3 queries and find out 3 values.

```
1 2
1 3
2 3
```

From here we can get the individual values of a[1], a[2], and a[3].


```py
from pwn import remote

r = remote('secretarray.fword.wtf', 1337)

x = r.recvuntil('START:\n').decode()
print(x)

arr = []

for k in range(0, 1335, 3):
    x = f'{k} {k+1}'
    print(x)
    x = r.sendline(x)
    a = int(r.recvline().decode())
    print(a)

    x = f'{k+1} {k+2}'
    print(x)
    x = r.sendline(x)
    b = int(r.recvline().decode())
    print(b)

    x = f'{k} {k+2}'
    print(x)
    x = r.sendline(x)
    c = int(r.recvline().decode())
    print(c)

    first = (a - b + c)//2
    second = a - first
    third = b - second

    arr.append(first)
    arr.append(second)
    arr.append(third)

x = f'{1334} {1335}'
r.sendline(x)
x = int(r.recvline().decode())
first = x - arr[1334]
arr.append(first)

x = f'{1334} {1336}'
r.sendline(x)
x = int(r.recvline().decode())
first = x - arr[1334]
arr.append(first)

print(arr)

r.sendline('DONE {}'.format(' '.join(map(str, arr))))
x = r.recvline().decode()

print(x)
```

The flag is:

```
FwordCTF{R4nd0m_isnT_R4nd0m_4ft3r_4LL_!_Everyhthing_is_predict4bl3_1f_y0u_kn0w_wh4t_Y0u_d01nGGGG}
```