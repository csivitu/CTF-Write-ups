# base646464

Author: [roerohan](https://github.com/roerohan)

Base 64, base 64, base 64 ... 25 times.

# Requirements

- Basic Knowledge of Node.js

# Source

- [generate.js](./generate.js)
- [cipher.txt](./cipher.txt)

# Exploitation

You have to decode base64 25 times.

```javascript
// Flag is base 64 encoded 25 times
let ret = flag;
for(let i = 0; i < 25; i++) ret = btoa(ret);
```

Of course, you can use bash XD:

```bash
cat cipher.txt | base64 -d | base64 -d |base64 -d | base64 -d 
| base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | ba
se64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64
 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d 
| base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
flag{l00ks_l1ke_a_l0t_of_64s}
```

You can use python too:

```python
>>> f = open('cipher.txt').read()
>>> import base64
>>> for i in range(25):
...     f = base64.b64decode(f)
... 
>>> print(f)
b'flag{l00ks_l1ke_a_l0t_of_64s}'
```

The flag is:

```
flag{l00ks_l1ke_a_l0t_of_64s}
```