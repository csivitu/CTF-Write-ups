# Perfect Secrecy

Author: [roerohan](https://github.com/roerohan) and [thebongy](https://github.com/thebongy)

# Requirements

- Python

# Source

- [image1.png](./image1.png)
- [image2.png](./image2.png)

```
Alice sent over a couple of images with sensitive information to Bob, encrypted with a pre-shared key. It is the most secure encryption scheme, theoretically...
```

# Exploitation

This challenge took a bit of guessing, but if you XOR every pixel from `image1` with every pixel from `image2` and save that image, you get the [result.png](./result.png) image which has a base64 string that can be decoded to get the flag.
<br />

You can get the image using:

```py
from PIL import Image
import numpy as np

def read_image(imPath):
    im = Image.open(imPath)

    pix_val = list(map(lambda x: int(x != 0), im.getdata()))
    return pix_val

data1 = read_image('image1.png')
data2 = read_image('image2.png')

res = [None] * len(data1)

for i in range(len(res)):
    if data1[i] ^ data2[i] == 1:
        res[i] = 1
    else:
        res[i] = 0

array = np.array(res, dtype=np.uint8)
im = np.reshape(array,(256,256))

img = Image.fromarray(np.uint8(im * 255) , 'L')
img.save('./result.png')

print('Written successfully.')

"""
echo ZmxhZ3swbjNfdDFtM19QQGQhfQ== | base64 -d
flag{0n3_t1m3_P@d!}
"""
```

Once you get this, you can decode the base64 string with the help of `base64` in linux.

```bash
echo ZmxhZ3swbjNfdDFtM19QQGQhfQ== | base64 -d
flag{0n3_t1m3_P@d!}
```

The flag is:

```
flag{0n3_t1m3_P@d!}
```
