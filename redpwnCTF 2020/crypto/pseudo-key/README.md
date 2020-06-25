# pseudo-key

Author: [roerohan](https://github.com/roerohan)

Basic reversing challenge.

# Requirements

- Python

# Source

- [pseudo-key.py](./pseudo-key.py)
- [pseudo-key-output.txt](./pseudo-key-output.txt)

```
Keys are not always as they seem...

Note: Make sure to wrap the plaintext with flag{} before you submit!
```

```python
#!/usr/bin/env python3

from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

def encrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x + y) % 26]
    return ctxt

with open('flag.txt') as f, open('key.txt') as k:
    flag = f.read()
    key = k.read()

ptxt = flag[5:-1]

ctxt = encrypt(ptxt,key)
pseudo_key = encrypt(key,key)

print('Ciphertext:',ctxt)
print('Pseudo-key:',pseudo_key)

```

# Exploitation

The most important function is of course, the `encrypt` function.

```
def encrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x + y) % 26]
```

This takes `ptxt` and `key`, makes `key` match the size of `ptxt` by repeating characters in a cyclic fashion, then adds the number equivalent (a->0, z->25) of each character of `key` to that of `ptxt` and mods it with 26. This value is converted to the corresponding character.
<br />

There is also a pseudo key along with this file. The pseudo key is made by encrypting the `key` using the `key` itself. 

```python
pseudo_key = encrypt(key,key)
```

Which means, there might be many possible keys (because of the %26). However, we can get all possible characters in the key by adding 26 and by not adding 26 to the number equivalent of each character:

```python
def get_key(pkey):
    x = ''
    y = ''
    for i in range(len(pkey)):
        c = chr_to_num[pkey[i]]
        x += num_to_chr[c/2]
        y += num_to_chr[(c+26)/2]
    print(x)
    print(y)
```

This gives us 2 strings:

```
eedcjjjacgf
rrqpwwwnpts
```

If you see carefully, you can combine these 2 keys to get `redpwwwnctf` (first character from key2, second and third from key1, and so on...), which seems like it's going to be the correct key. (Yes, it's sort of a guess)

Now, we can simply use almost exactly the same function to decrypt the key, except, here you subtract instead of adding:

```python
from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}

num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}
ctxt = 'z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut'
pseudo_key = 'iigesssaemk'

def get_key(pkey):
    x = ''
    y = ''
    for i in range(len(pkey)):
        c = chr_to_num[pkey[i]]
        x += num_to_chr[c/2]
        y += num_to_chr[(c+26)/2]
    print(x)
    print(y)

get_key(pseudo_key)

key = 'redpwwwnctf'

def decrypt(ct, key):
    flag = ''
    key = ''.join(key[i % len(key)] for i in range(len(ct))).lower()
    for i in range(len(ct)):
        if ct[i] == '_':
            flag += '_'
            continue
        flag += num_to_chr[(chr_to_num[ct[i]] - chr_to_num[key[i]]) % 26]
    print(flag)
decrypt(ctxt, key)
```

You can run this using python to get the flag.

```bash
$ python pseudo-key/crack.py 
eedcjjjacgf
rrqpwwwnpts
i_guess_pseudo_keys_are_pseudo_secure
```

The flag is:

```
flag{i_guess_pseudo_keys_are_pseudo_secure}
```