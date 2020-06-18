# arg1

Author: [roerohan](https://github.com/roerohan)

This challenge can be solved using `strings`.

# Requirements

- Linux `strings` command

# Source

- [arg01](./arg01)
- [Reverse Engineering](http://cyberhomectf.eastus.cloudapp.azure.com/challenges?category=reverse-engineering)

# Exploitation

This is a simple challenge, the key is hidden in the file as a string. Use the `strings` command in linux and find it.

```bash
$ strings ./CyberHome\ CTF/Reverse\ Engineering/arg01/arg01
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
printf
__cxa_finalize__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u/UH
[]A\A]A^A_
Need exactly one argument.
R3v3r53_15_7h3_B35T
No, %s is not correct.
Yes, %s is correct!
```

Notice the `R3v3r53_15_7h3_B35T` string.

```bash
arg01 R3v3r53_15_7h3_B35T
Yes, R3v3r53_15_7h3_B35T is correct!
```

Wrap this string in `cbrh{}`. The flag is:

```
cbrh{R3v3r53_15_7h3_B35T}
```
