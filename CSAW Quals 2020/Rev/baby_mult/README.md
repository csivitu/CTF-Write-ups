# baby_mult

Author: [roerohan](https://github.com/roerohan)

# Requirements

- C
- GDB

# Source

- [program.txt](./program.txt)

```
Welcome to reversing! Prove your worth and get the flag from this neat little program!
```

# Exploitation

The following numbers are written in `program.txt`.

```
85, 72, 137, 229, 72, 131, 236, 24, 72, 199, 69, 248, 79, 0, 0, 0, 72, 184, 21, 79, 231, 75, 1, 0, 0, 0, 72, 137, 69, 240, 72, 199, 69, 232, 4, 0, 0, 0, 72, 199, 69, 224, 3, 0, 0, 0, 72, 199, 69, 216, 19, 0, 0, 0, 72, 199, 69, 208, 21, 1, 0, 0, 72, 184, 97, 91, 100, 75, 207, 119, 0, 0, 72, 137, 69, 200, 72, 199, 69, 192, 2, 0, 0, 0, 72, 199, 69, 184, 17, 0, 0, 0, 72, 199, 69, 176, 193, 33, 0, 0, 72, 199, 69, 168, 233, 101, 34, 24, 72, 199, 69, 160, 51, 8, 0, 0, 72, 199, 69, 152, 171, 10, 0, 0, 72, 199, 69, 144, 173, 170, 141, 0, 72, 139, 69, 248, 72, 15, 175, 69, 240, 72, 137, 69, 136, 72, 139, 69, 232, 72, 15, 175, 69, 224, 72, 15, 175, 69, 216, 72, 15, 175, 69, 208, 72, 15, 175, 69, 200, 72, 137, 69, 128, 72, 139, 69, 192, 72, 15, 175, 69, 184, 72, 15, 175, 69, 176, 72, 15, 175, 69, 168, 72, 137, 133, 120, 255, 255, 255, 72, 139, 69, 160, 72, 15, 175, 69, 152, 72, 15, 175, 69, 144, 72, 137, 133, 112, 255, 255, 255, 184, 0, 0, 0, 0, 201
```

These are actually bytes of a piece of shell code in integer. You can write a simple C program to run the shell code.

```c
#include<stdio.h>
#include<string.h>

main()
{
  unsigned char code[] = "\x55\x48\x89\xe5\x48\x83\xec\x18\x48\xc7\x45\xf8\x4f\x00\x00\x00\x48\xb8\x15\x4f\xe7\x4b\x01\x00\x00\x00\x48\x89\x45\xf0\x48\xc7\x45\xe8\x04\x00\x00\x00\x48\xc7\x45\xe0\x03\x00\x00\x00\x48\xc7\x45\xd8\x13\x00\x00\x00\x48\xc7\x45\xd0\x15\x01\x00\x00\x48\xb8\x61\x5b\x64\x4b\xcf\x77\x00\x00\x48\x89\x45\xc8\x48\xc7\x45\xc0\x02\x00\x00\x00\x48\xc7\x45\xb8\x11\x00\x00\x00\x48\xc7\x45\xb0\xc1\x21\x00\x00\x48\xc7\x45\xa8\xe9\x65\x22\x18\x48\xc7\x45\xa0\x33\x08\x00\x00\x48\xc7\x45\x98\xab\x0a\x00\x00\x48\xc7\x45\x90\xad\xaa\x8d\x00\x48\x8b\x45\xf8\x48\x0f\xaf\x45\xf0\x48\x89\x45\x88\x48\x8b\x45\xe8\x48\x0f\xaf\x45\xe0\x48\x0f\xaf\x45\xd8\x48\x0f\xaf\x45\xd0\x48\x0f\xaf\x45\xc8\x48\x89\x45\x80\x48\x8b\x45\xc0\x48\x0f\xaf\x45\xb8\x48\x0f\xaf\x45\xb0\x48\x0f\xaf\x45\xa8\x48\x89\x85\x78\xff\xff\xff\x48\x8b\x45\xa0\x48\x0f\xaf\x45\x98\x48\x0f\xaf\x45\x90\x48\x89\x85\x70\xff\xff\xff\xb8\x00\x00\x00\x00\xc9";
  int (*ret)() = (int(*)())code;

  ret();
}
```

Now, open the file in `gdb` and break at let it run the shellcode. Stop at the end of the shellcode and observe the stack. It would look like:

```
0x7fffffffdbc0: 0x72346d7d      0x00003067      0x645f7072      0x00006c31
0x7fffffffdbd0: 0x725f7634      0x73757033      0x6c61677b      0x00000066
0x7fffffffdbe0: 0x008daaad      0x00000000      0x00000aab      0x00000000
0x7fffffffdbf0: 0x00000833      0x00000000      0x182265e9      0x00000000
0x7fffffffdc00: 0x000021c1      0x00000000      0x00000011      0x00000000
0x7fffffffdc10: 0x00000002      0x00000000      0x4b645b61      0x000077cf
0x7fffffffdc20: 0x00000115      0x00000000      0x00000013      0x00000000
0x7fffffffdc30: 0x00000003      0x00000000      0x00000004      0x00000000
```

Read the string from the stack, you would get the following flag

```
flag{sup3r_v4l1d_pr0gr4m}
```