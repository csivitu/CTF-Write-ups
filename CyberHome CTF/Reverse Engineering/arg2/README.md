# arg2

Author: [roerohan](https://github.com/roerohan)

This challenge can be solved by seeing the decompiled C code.

# Requirements

- Linux `strings` command
- Ghidra

# Source

- [arg2](./arg2)
- [Reverse Engineering](http://cyberhomectf.eastus.cloudapp.azure.com/challenges?category=reverse-engineering)

# Exploitation

When you decompile the program in `ghidra`, you get the following code:

```c

undefined8 main(int param_1,long param_2)

{
  char cVar1;
  char cVar2;
  undefined8 uVar3;
  long lVar4;
  
  if (param_1 == 2) {
    cVar2 = 'D';
    lVar4 = 0;
    do {
      cVar1 = *(char *)(*(long *)(param_2 + 8) + lVar4);
      if (cVar1 == '\0') break;
      if ((int)cVar2 + -2 != (int)cVar1) {
        printf("No, %s is not correct.\n");
        return 1;
      }
      cVar2 = "j4e_AP34710L_15_Z0PPPPGLE"[lVar4];
      lVar4 = lVar4 + 1;
    } while (cVar2 != '\0');
    printf("Yes, %s is correct!\n");
    uVar3 = 0;
  }
  else {
    puts("Need exactly one argument.");
    uVar3 = 0xffffffff;
  }
  return uVar3;
}
```

Here you can see that the input is being rotated backwards by a shift of 2, and matched with the string `Dj4e_AP34710L_15_Z0PPPPGLE` (like a Caesar's Cipher). So once you rotate every character in this string forward by 2 (or backwards by 24) you get:

```
Fl4g_CR34710N_15_B0RRRRING
```

To get the correct flag, wrap this in `cbrh{}`. The flag is:

```
cbrh{Fl4g_CR34710N_15_B0RRRRING}
```
