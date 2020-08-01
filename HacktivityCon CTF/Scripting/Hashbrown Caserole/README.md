# Hashbrown Caserole

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Python

# Source

```
Hashbrowns

Connect here:
nc jh2i.com 50005
```

# Exploitation

```python
import hashlib
from pwn import remote

r = remote('jh2i.com', 50005)

def match_sha1(n):
    for i in range(0, 10**8):
        if i%1000000 == 0: print(i)
        if(hashlib.sha1(str(i).encode()).hexdigest()[:len(n)] == n): 
            return i

def match_md5(n):
    for i in range(0, 10**8):
        if i%1000000 == 0: print(i)
        if(hashlib.md5(str(i).encode()).hexdigest()[:len(n)] == n): 
            return i

while True:
    t = 'md5'
    x = r.recv(1024).decode().strip()
    print(x)

    if 'sha1' in x:
        t = 'sha1'

    if ('flag' in x): break

    x = x.split(': ')[1]

    res = 0
    if t == 'md5':
        res = match_md5(x)
    else:
        res = match_sha1(x)

    r.sendline(str(res))
    print('Sending: ' + str(res))
    print(r.recvline().decode())
```

This is probably not the most efficient script, you could create a reverse dictionary and map it directly, but this works too. The script runs for several minutes and gives you the flag.

```bash
$ python script.py
...
...
That casserole was DELICIOUS!!!! Here's your flag: flag{warm_casseroles_for_breakfast!!!}
```


The flag is:

```
flag{warm_casseroles_for_breakfast!!!}
```