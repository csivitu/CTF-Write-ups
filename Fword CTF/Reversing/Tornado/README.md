# Secret Array

Author: [thebongy](https://github.com/thebongy) and [roerohan](https://github.com/roerohan)

# Requirements

- Python

# Source

```
Get back to flag.

Author: KOOLI
```

# Exploitation

Since we have the AES key, it's got nothing much to do with that. We just have to reverse the shuffling properly.

```py
#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
from binascii import hexlify
import random

key = "very_awes0m3_k3y"
flag = "FwordCTF{xxx_xxx}" #REDACTED
# assert len(flag) == 62
# assert len(key) == 16

def to_blocks(text):
	return [text[i*2:(i+1)*2].encode() for i in range(len(text)//2)]

def random_bytes(seed):
	random.seed(seed)
	return long_to_bytes(random.getrandbits(8*16))

def encrypt_block(block,key):
	cipher = AES.new(key.encode(), AES.MODE_ECB)
	plain_pad = pad(block, 16)
	return hexlify(cipher.encrypt(plain_pad)).decode()

def encrypt(txt, key):
	res = ""
	blocks = to_blocks(txt)
	for block in blocks:
		res += encrypt_block(block, key)
	return res

def decrypt(txt, key):
	b = bytes.fromhex(txt)
	flag = b''
	for i in range(0, len(b), 16):
		block = b[i:i+16]
		cipher = AES.new(key.encode(), AES.MODE_ECB)
		dec = cipher.decrypt(block)
		flag += dec[:2]
	return flag
		
def translate(txt,l,r):
	return txt[:l]+txt[r:]+txt[l:r]

def reverse_translate(txt, l, r):
	return txt[:l] + txt[-(r-l):] + txt[l:(-(r-l))]

def shuffle(txt):
	seed=random.choice(txt)
	random.seed(seed)
	for _ in range(45):
		l = random.randint(0, 15)
		r = random.randint(l+1, 33)
		txt = translate(txt, l, r)
	return txt

def reverse_shuffle(txt, seed):
	random.seed(seed)
	vals = []
	for _ in range(45):
		l = random.randint(0, 15)
		r = random.randint(l+1, 33)
		vals.append((l,r))
	
	vals = vals[::-1]
	for i in range(45):
		txt = reverse_translate(txt, vals[i][0], vals[i][1])
	return txt

flag = shuffle(flag)
print (encrypt(flag, key))


hx = '3ce29d5f8d646d853b5f6677a564aec6bd1c9f0cbfac0af73fb5cfb446e08cfec5a261ec050f6f30d9f1dfd85a9df875168851e1a111a9d9bfdbab238ce4a4eb3b4f8e0db42e0a5af305105834605f90621940e3f801e0e4e0ca401ff451f1983701831243df999cfaf40b4ac50599de5c87cd68857980a037682b4dbfa1d26c949e743f8d77549c5991c8e1f21d891a1ac87166d3074e4859a26954d725ed4f2332a8b326f4634810a24f1908945052bfd0181ff801b1d3a0bc535df622a299a9666de40dfba06a684a4db213f28f3471ba7059bcbdc042fd45c58ae4970f53fb808143eaa9ec6cf35339c58fa12efa18728eb426a2fcb0234d8539c0628c49b416c0963a33e6a0b91e7733b42f29900921626bba03e76b1911d20728254b84f38a2ce12ec5d98a2fa3201522aa17d6972fe7c04f1f64c9fd4623583cc5a91cc471a13d6ab9b0903704727d1eb987fd5d59b5757babb92758e06d2f12fd7e32d66fe9e3b9d11cd93b11beb70c66b57af71787457c78ff152ff4bd63a83ef894c1f01ae476253cbef154701f07cc7e0e16f7eede0c8fa2d5a5dd5624caa5408ca74b4b8c8f847ba570023b481c6ec642dac634c112ae9fec3cbd59e1d2f84f56282cb74a3ac6152c32c671190e2f4c14704ed9bbe74eaafc3ce27849533141e9642c91a7bf846848d7fbfcd839c2ca3b'

chars = decrypt(hx, key)

possible_seeds = list(map(chr, set(chars)))
for i in possible_seeds:
	print(reverse_shuffle(chars, i))
```

Run the script with python.

```bash
$ python solve-tornado.py | grep Fword
```

The flag is:

```
FwordCTF{peekaboo_i_am_the_flag_!_i_am_the_danger_52592bbfcd8}
```