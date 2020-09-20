# Hex Cipher Shift

Author: [roerohan](https://github.com/roerohan)

## Source

```
People say shift ciphers aren't secure. I'm here to prove them wrong!
```

```py
from random import shuffle
from secret import secret_msg

ALPHABET = '0123456789abcdef'

class Cipher:
    def __init__(self, key):
        self.key = key
        self.n = len(self.key)
        self.s = 7

    def add(self, num1, num2):
        res = 0
        for i in range(4):
            res += (((num1 & 1) + (num2 & 1)) % 2) << i
            num1 >>= 1
            num2 >>= 1
        return res

    def encrypt(self, msg):
        key = self.key
        s = self.s
        ciphertext = ''
        for m_i in msg:
            c_i = key[self.add(key.index(m_i), s)]
            ciphertext += c_i
            s = key.index(m_i)
        return ciphertext

plaintext = b'The secret message is:'.hex() + secret_msg.hex()

key = list(ALPHABET)
shuffle(key)

cipher = Cipher(key)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

# output:
# 85677bc8302bb20f3be728f99be0002ee88bc8fdc045b80e1dd22bc8fcc0034dd809e8f77023fbc83cd02ec8fbb11cc02cdbb62837677bc8f2277eeaaaabb1188bc998087bef3bcf40683cd02eef48f44aaee805b8045453a546815639e6592c173e4994e044a9084ea4000049e1e7e9873fc90ab9e1d4437fc9836aa80423cc2198882a
```

## Exploit

The first thing I noticed was this function:

```py
def add(self, num1, num2):
    res = 0
    for i in range(4):
        res += (((num1 & 1) + (num2 & 1)) % 2) << i
        num1 >>= 1
        num2 >>= 1
    return res
```

If you observe this, it is actually doing just `num1 XOR num2` (modulo 2 addition of individual bytes and shifting). You can confirm this by comparing it's output with the `^` operator in Python.

```py
>>> 5 ^ 7
2
>>> add(5,7)
2
```

You can also easily reverse the `encrypt` function to write a `decrypt` function, as follows:

```py
def decrypt(ciphertext, key):
    s = 7
    plaintext = ''
    for i in range(len(ciphertext)):
        p = key[key.index(ciphertext[i]) ^ s]
        s = key.index(ciphertext[i]) ^ s
        plaintext += p

    return plaintext
```

Now, the only issue is that we do not know the `key`. But, from the `encrypt` function, we know that the ciphertext is produced in the following manner:

```py
c_i = key[key.index(m_i) ^ s]
ciphertext += c_i
s = key.index(m_i)
```

The plaintext in hex is `54686520736563726574206d6573736167652069733a`. Using this, the ciphertext, and the initial value of `s`, we can say that for each character, the following rule must apply.

```
k.index('character in ciphretext') = k.index('character in plaintext') ^ k.index('previous character in plaintext')
```

For example, we can deduce these rules.

```py
k.index('8') = k.index('5') ^ 7
k.index('5') = k.index('4') ^ k.index('5')
k.index('6') = k.index('6') ^ k.index('4')
k.index('7') = k.index('8') ^ k.index('6')
k.index('7') = k.index('6') ^ k.index('8')

and so on...
```

An observation: We can see that `k.index('5') = k.index('4') ^ k.index('5')`, or `k.index('4')` must be 0, which is later verified by the following rules too:

```py
k.index('7') = k.index('4') ^ k.index('7')
k.index('2') = k.index('2') ^ k.index('4')

and so on...
```

Now, we need to find the key that satisfies all the rules. So, I first generated all the rules using the following function:

```py
def gen_rules(ciphertext, plaintext):
    x = plaintext
    y = ciphertext[:len(plaintext)]
    s = 7

    xor_rules = []
    xor_res = []
    for i in range(len(plaintext)):
        tmp = f"k.index('{x[i]}') ^ {s} = k.index('{y[i]}')".split(' = ')
        xor_rules.append(tmp[0])
        xor_res.append(tmp[1])
        s = f"k.index('{x[i]}')"
    
    return xor_rules, xor_res
```

Now, I keep swapping elements in the key until the decrypt function returns back the `plaintext` I passed as input. If it doesn't (because earlier rules may be violated in later swaps), I rotate they key and try again.

```py
def get_key(xor_rules, xor_res, plaintext):
    k = list(ALPHABET)

    while plaintext not in decrypt(ciphertext, k):
        k = rotate(k, 1)

        for i in range(len(xor_rules)):
            xorred = eval(xor_rules[i])

            if xorred != eval(xor_res[i]):
                tmp = k[xorred]
                tmp_ind = eval(xor_res[i])
            
                k[xorred] = xor_res[i][9]
                k[tmp_ind] = tmp
    return k
```

This returns the key.

```
4802dc51a9eb763f
```

> Note: As predicted, the first character is `4`.

Now, decrypt the ciphertext with the key and get your flag. Here is a script which does all the steps for you.


```py
ALPHABET = '0123456789abcdef'

def gen_rules(ciphertext, plaintext):
    x = plaintext
    y = ciphertext[:len(plaintext)]
    s = 7

    xor_rules = []
    xor_res = []
    for i in range(len(plaintext)):
        tmp = f"k.index('{x[i]}') ^ {s} = k.index('{y[i]}')".split(' = ')
        xor_rules.append(tmp[0])
        xor_res.append(tmp[1])
        s = f"k.index('{x[i]}')"
    
    return xor_rules, xor_res

def decrypt(ciphertext, key):
    s = 7
    plaintext = ''
    for i in range(len(ciphertext)):
        p = key[key.index(ciphertext[i]) ^ s]
        s = key.index(ciphertext[i]) ^ s
        plaintext += p

    return plaintext

def rotate(l, n):
    return l[-n:] + l[:-n]

def get_key(xor_rules, xor_res, plaintext):
    k = list(ALPHABET)

    while plaintext not in decrypt(ciphertext, k):
        k = rotate(k, 1)

        for i in range(len(xor_rules)):
            xorred = eval(xor_rules[i])

            if xorred != eval(xor_res[i]):
                tmp = k[xorred]
                tmp_ind = eval(xor_res[i])
            
                k[xorred] = xor_res[i][9]
                k[tmp_ind] = tmp
    return k


plaintext = b'The secret message is:'.hex()

ciphertext = '85677bc8302bb20f3be728f99be0002ee88bc8fdc045b80e1dd22bc8fcc0034dd809e8f77023fbc83cd02ec8fbb11cc02cdbb62837677bc8f2277eeaaaabb1188bc998087bef3bcf40683cd02eef48f44aaee805b8045453a546815639e6592c173e4994e044a9084ea4000049e1e7e9873fc90ab9e1d4437fc9836aa80423cc2198882a'

xor_rules, xor_res = gen_rules(ciphertext, plaintext)

k = get_key(xor_rules, xor_res, plaintext)

print('[Key]\n' + ''.join(k))
msg = decrypt(ciphertext, k)
print('[MESSAGE]\n' + bytes.fromhex(msg).decode())
```

Run it with `python3`.

```bash
$ python exploit.py 
[Key]
4802dc51a9eb763f
[MESSAGE]
The secret message is: Nice job! I hope you enjoyed the challenge. Here's your flag: DUCTF{d1d_y0u_Us3_gu3ss1nG_0r_l1n34r_4lg3bRA??}
```

The flag is:

```
DUCTF{d1d_y0u_Us3_gu3ss1nG_0r_l1n34r_4lg3bRA??}
```
