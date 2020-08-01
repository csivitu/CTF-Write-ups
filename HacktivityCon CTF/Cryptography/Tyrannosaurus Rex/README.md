# Tyrannosaurus Rex

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Python

# Source

```python
#!/usr/bin/env python

import base64
import binascii

h = binascii.hexlify
b = base64.b64encode

c = b'37151032694744553d12220a0f584315517477520e2b3c226b5b1e150f5549120e5540230202360f0d20220a376c0067'

def enc(f):
    e = b(f)

    print(e)
    z = []
    i = 0
    while i < len(e):
        z += [ e[i] ^ e[((i + 1) % len(e))]]
        i = i + 1
    print(z)
    print(bytearray(z))
    c = h(bytearray(z))
    return c
```

```
We found this fossil. Can you reverse time and bring this back to life?
```

# Exploitation

In this challenge, you have to reverse the steps to get back the original flag from the ciphertext `c`. Make a function `dec(x)` which takes in the ciphertexts and spits out the original text.

```python
#!/usr/bin/env python

import base64
import binascii

h = binascii.hexlify
b = base64.b64encode

c = b'37151032694744553d12220a0f584315517477520e2b3c226b5b1e150f5549120e5540230202360f0d20220a376c0067'

def enc(f):
    e = b(f)

    print(e)
    z = []
    i = 0
    while i < len(e):
        z += [ e[i] ^ e[((i + 1) % len(e))]]
        i = i + 1
    print(z)
    print(bytearray(z))
    c = h(bytearray(z))
    return c

def dec(x):
    x = list(bytes.fromhex(x.decode()))
    z = ord('Z')
    for i in range(len(x)):
        print(chr(z), end='')
        z = x[i] ^ z
dec(c)
```

Now, just run this with python, and pipe the output to `base64 -d`.

```bash
$ python fossil | base64 -d
flag{tyrannosauras_xor_in_reverse}
```

The flag is:
```
flag{tyrannosauras_xor_in_reverse}
```