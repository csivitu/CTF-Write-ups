# Hungry Man - Web

Author - [UnknownAbyss](https://github.com/UnknownAbyss)

Requirements : Python, cURL

* * *

The challenge gives us the following text -

> There is nothing here I promise! ;)


```
very.uniquename.xyz:2095
```

#### Upon opening the link we see -

<p align="center"><img src="https://i.imgur.com/HsXPiDO.png" alt="Chall Image"></p>


Checking the network tab, we find the following response header

<p align="center"><img src="https://i.imgur.com/sYB2iGY.png" alt="Chall Image"></p>

We send the following curl request setting the cookie to the given string

```sh
curl -H "Cookie: flag=c29tZXRpbWVzIHRoZSBrZXkgdG8gdW5sb2NraW5nIHRoZSBhbnN3ZXIgaXMgdGhlIHF1ZXN0aW9uIGl0c2VsZi4uLiBidXQgbXkgZmF2b3JpdGUgaXMgY2hvY28gY2hpcA==" very.uniquename.xyz:2095
```

The repsonse is...

```
{"flag":"522748524ad010358705b6852b81be4c"}
```

Then sending this new cookie...

```sh
curl -H "Cookie: flag=522748524ad010358705b6852b81be4c" very.uniquename.xyz:2095
```

The repsonse is...

```
{"flag":"70e9490b5d5a217070c1e7df9518e9d5"}
```

Let us write a script for this...

```py
import requests


url = 'http://very.uniquename.xyz:2095'
flags = ['c29tZXRpbWVzIHRoZSBrZXkgdG8gdW5sb2NraW5nIHRoZSBhbnN3ZXIgaXMgdGhlIHF1ZXN0aW9uIGl0c2VsZi4uLiBidXQgbXkgZmF2b3JpdGUgaXMgY2hvY28gY2hpcA==']


while (flags[-1]!='EOF'):
    x = requests.get(url, cookies={'flag': flags[-1]}).text
    flags.append(x[9:-3 ])

for i in flags[1:-1]:
    print(i)
```

This gives us the following output

```
522748524ad010358705b6852b81be4c
70e9490b5d5a217070c1e7df9518e9d5
60173ca988f93d0a7da64f3327ad336c
45ec864b6976a208c6af1a37e2c61c3a
046bf0a7d0d641c527765a02816eca9f
24cafc74b88dfafb0524ecc85a76f8bd
f3ea97d2cd1f5619f570c06a10a041b5
fa4f4d80f554c6845daf73511d75e6bc
72e6f6e0f08ca88f02b1480464afd55b
97d243cd9c2513d20fff6d5677b2b62b
ffc987113c7a22fb2a52b6f9842f79be
a61c8204ca3eb98c9da7344cf0fba066
9bea76c2f9cb9140f837ee4518b6749c
```

This appears to be an MD5 hash. We decode these and find the following string

```
ds
c{
91v
3_m
3_4
_h
4n
dfu
1_0
f_
c00
k13
5}
```

This is the flag...
```
dsc{91v3_m3_4_h4ndfu1_0f_c00k135}
```