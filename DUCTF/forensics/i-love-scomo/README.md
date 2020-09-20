# I Love Scomo

Author: [roerohan](https://github.com/roerohan)

## Source

```
I really do love Scott Morrison! <3 <3 <3

However, some people don't like me because of my secret crush :(. So I have to hide my secrets using steganography. This is my hidden space, where I can dream about being with Scomo and I really appreciate that no one tries to reveal my secret message for him.
```

## Exploit

In the challenge description, `hidden space` was in bold. This might be useful later.
<br />

First, you can use `stegcrack` to extract a `txt` file out of the image. The `txt` file is present in [ilovescomo.jpg.out](./ilovescomo.jpg.out).

In this, you will notice that some lines have a white space in the end, and some do not. This makes sense because `hidden space` was written in bold in the description. We assume that a white space means `1` and the absence of a white space means `0`. Then we convert the obtained binary string to ASCII to get the flag.

```py
# Get ilovescomo.jpg.out using stegcrack
text = open('./ilovescomo.jpg.out', 'r').read().split('\n')

l = ['0'] * len(text)

for i in range(len(text)):
    if text[i] == '':
        continue
    if text[i][-1] == ' ':
        l[i] = '1'

print(''.join(l))

l = [chr(int(''.join(l[i:i+8]), 2)) for i in range(0, len(l), 8)]

print(''.join(l))
```