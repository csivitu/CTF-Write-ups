# Snakes Everywhere

Author: [roerohan](https://github.com/roerohan)

Disassemble Python byte code and reverse the obtained python code.

# Requirements

- Python 3
- Basic Knowledge of Python Byte Code

# Source

- https://ctf.zh3r0.ml/challenges#snakes%20everywhere

```
Can a snake go backwards

Author : Whit3_D3vi1

Files: py_dis1, snake.txt
```
- [py_dis1](./py_dis1)
- [snake.txt](./snake.txt)


# Exploitation

The code you see in [`py_dis1`]('./py_dis1) is essentially python bytecode. The target in this challenge is to reverse this program and pass the string in [`snake.txt`](./py_dis1) as input, so that we get the flag.
<br />

But before that, we need to find out what the program does. We could not find a decompiler for the program, so we did it manually :laughing:. Here's a bit on how to interpret this bytecode.

```
  2           0 LOAD_CONST               0 (0)
              2 LOAD_CONST               1 (('flag1',))
              4 IMPORT_NAME              0 (flags)
              6 IMPORT_FROM              1 (flag1)
              8 STORE_NAME               1 (flag1)
             10 POP_TOP

  3          12 LOAD_NAME                1 (flag1)
             14 STORE_NAME               2 (flag)

  4          16 LOAD_CONST               2 ('zh3r0{fake flag}')
             18 STORE_NAME               3 (fake_flag)

  6          20 LOAD_CONST               3 ('I_l0v3_r3v3r51ng')
             22 STORE_NAME               4 (key)
```

Reading bytecode is pretty intuitive (unlike assembly). Here, it first loads the constants `0` and `('flag1',)` in memory. Then imports flag etc. The part we care about starts at:

```
  3          12 LOAD_NAME                1 (flag1)
             14 STORE_NAME               2 (flag)

  4          16 LOAD_CONST               2 ('zh3r0{fake flag}')
             18 STORE_NAME               3 (fake_flag)

  6          20 LOAD_CONST               3 ('I_l0v3_r3v3r51ng')
             22 STORE_NAME               4 (key)
```

This stores `flag1` in variable `flag`, `zh3r0{fake flag}` in `fake_flag`, and `'I_l0v3_r3v3r51ng'` in `key`. So, this translates to,

```python
flag = 'zh3ro{fake flag}'
key = 'I_l0v3_r3v3r51ng'
```

Then, we get to know the size of the flag from here:

```
  8          24 LOAD_NAME                5 (len)
             26 LOAD_NAME                2 (flag)
             28 CALL_FUNCTION            1
             30 LOAD_CONST               4 (38)
             32 COMPARE_OP               2 (==)
             34 POP_JUMP_IF_TRUE        40
             36 LOAD_GLOBAL              6 (AssertionError)
             38 RAISE_VARARGS            1
```

So the length of the `flag` is 38. As you keep converting the bytecode to python (in a postfix fashion), you get the following python code ([guess.py](./guess.py)):

```python
flag = 'zh3ro{fake flag}'
key = 'I_l0v3_r3v3r51ng'

# flag size is 38

def xor(str1, str2):
    return chr(ord(str1)^ord(str2))

ciphertext = ''

for i in range(len(flag)//3):
    ciphertext += chr(ord(key[i]) * ord(flag[i]) - i)


for i in range(len(flag)//3, len(flag)//3 * 2):
    ciphertext += chr( ord(flag[i]) * ord(key[i%len(key)]) + i)

for i in range(len(key)//2, len(flag)):
    ciphertext += xor(key[i%16], flag[i])

file = open('ciphertext.txt', 'w')
print(len(ciphertext))

file.write(ciphertext)
file.close()
```

Cool, so now we know that the file we got as `snake.txt` is probably the `ciphertext`. So let's try to reverse this program and get the flag.
<br />

So we go over the loops in reverse. We know from a property of the `xor` operator that if `a xor b = c` then `c xor b = a`. So the last loop can reuse the same `xor` function during reversing. The goal is to find the `flag`, which by the way, has 38 characters. So you can just do:

```python
def xor(str1, str2):
    return chr(ord(str1)^ord(str2))

flag = [None]*38
key = 'I_l0v3_r3v3r51ng'

ciphertext = open('snake.txt').read()

k = len(ciphertext) - (len(flag) - len(key)//2)

for i in range(len(key)//2, len(flag)):
    flag[i] = xor(key[i%16], ciphertext[k])
    k += 1
```

This takes care of the last function, so we now take the last few characters from the ciphertext and decipher it, store it in `flag`. Similarly, the rest of the program is reversed. Here's the final reversed code ([rev.py](./rev.py)):

```python
def xor(str1, str2):
    return chr(ord(str1)^ord(str2))

flag = [None]*38
key = 'I_l0v3_r3v3r51ng'

ciphertext = open('snake.txt').read()

k = len(ciphertext) - (len(flag) - len(key)//2)

for i in range(len(key)//2, len(flag)):
    flag[i] = xor(key[i%16], ciphertext[k])
    k += 1

for i in range(len(flag)//3, len(flag)//3 * 2):
    flag[i] = chr((ord(ciphertext[i]) - i)//ord(key[i%len(key)]))


for i in range(len(flag)//3):
    flag[i] = chr((ord(ciphertext[i]) + i)//ord(key[i]))

print(''.join(flag))
```

When you run this program, you get:

```bash
$ python rev.py                                        
zh3r0{Python_disass3mbly_is v3ry_E4sy}
```

The flag is:

```                 
zh3r0{Python_disass3mbly_is v3ry_E4sy}
```