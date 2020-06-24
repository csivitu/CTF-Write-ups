# ropes

Author: [roerohan](https://github.com/roerohan)

This can be solved using `strings` in Linux.

# Requirements

- `strings` command

# Source

- [ropes](./ropes)
- [ropes (official)](https://redpwn.storage.googleapis.com/uploads/b896a5f99065a7df18d6ab3c6296c79f51f73ab0de3466944e08cbd2be4953fb/ropes)

# Exploitation

Run `strings` on the file to get the strings in the binary.

```bash
$ strings ropes
__PAGEZERO
__TEXT
__text
__TEXT
__stubs
__TEXT
__stub_helper
__TEXT
__cstring
__TEXT
__unwind_info
__TEXT
__DATA
__nl_symbol_ptr
__DATA
__la_symbol_ptr
__DATA
__LINKEDIT
/usr/lib/dyld
/usr/lib/libSystem.B.dylib
Give me a magic number: 
First part is: flag{r0pes_ar3_
Second part is: just_l0ng_str1ngs}
@dyld_stub_binder
@_printf
@_puts
@_scanf
_mh_execute_header
!main
__mh_execute_header
_main
_printf
_puts
_scanf
dyld_stub_binder
```

You can see there are 2 lines which contain the flag.

```
First part is: flag{r0pes_ar3_
Second part is: just_l0ng_str1ngs}
```

The flag is:

```
flag{r0pes_ar3_just_l0ng_str1ngs}