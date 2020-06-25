# 12-shades-of-redpwn

Author: [roerohan](https://github.com/roerohan)

Color wheel, base 12.

# Requirements

- Base 12

# Source

- [ciphertext.jpg](./ciphertext.jpg)
- [color-wheel.jpg](./color-wheel.jpg)

# Exploitation

Identify the colors from the ciphertext in the color-wheel, and use numbers 0-11 to write them (like in a clock).

```
86 90 81 87 a3 49 99 43 97 97 41 92 49 7b 41 97 7a 44 92 7a 44 96 98 a5
```

These are basically the values in base 12. Convert them to base 10, and then treat the values obtained as ASCII.

```python
>>> x = "86 90 81 87 a3 49 99 43 97 97 41 92 49 7b 41 97 7a 44 92 7a 44 96 98 a5"
>>> ''.join(list(map(lambda i: chr(int(i,12)), x.split())))
'flag{9u3ss1n9_1s^4n^4rt}'
```

Maybe we read some colors wrong? Replace the `^`s with `_`s. 
<br />

The flag is:

```
flag{9u3ss1n9_1s_4n_4rt}
```