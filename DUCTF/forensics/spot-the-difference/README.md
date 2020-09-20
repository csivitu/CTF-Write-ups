# Spot the Difference

Author: [roerohan](https://github.com/roerohan)

## Source

```
Author: TheDon

An employee's files have been captured by the first responders. The suspect has been accused of using images to leak confidential infomation, steghide has been authorised to decrypt any images for evidence!
```

## Exploit

Upon unzipping, you can see a broken png called `Publish/.config/Reminder.png`. When you check it's hexdump, you notice that the first 4 bytes of the `png` are not correct. Fix them using `hexedit Reminder.png` to make them `89 50 4E 47`.

```
00000000   89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  .PNG........
0000000C   49 48 44 52  00 00 02 F6  00 00 00 28  IHDR.......(
00000018   08 06 00 00  00 95 4A BE  56 00 00 0F  ......J.V...
00000024   94 49 44 41  54 78 01 ED  9D BB 6E E3  .IDATx....n.
00000030   3C 16 C7 8F  17 DF 43 EC  F6 36 06 53  <.....C..6.S
0000003C   E4 01 EC 07  58 20 C1 14  53 A5 9C 52  ....X ..S..R
00000048   E9 16 71 91  62 17 48 95  32 85 D3 C6  ..q.b.H.2...
```

Now, you can see the png. The password contains `1cmVQ`. There are a lot of base64 strings in `Public/.config/secret/`. Use grep to find the right string.

```bash
$ grep -rs 1cmVQ
31/5.txt:CjEyMzRJc0FTZWN1cmVQYXNzd29yZA==
```

Decode this to find the password.

```bash
$ echo CjEyMzRJc0FTZWN1cmVQYXNzd29yZA== | base64 -d

1234IsASecurePassword
```

Now, go through all the files in `Publish/badfiles` and extract them using steghide with the obtained password. One of them will give you a file, which you can read to get the flag.

```py
import os
import subprocess
password = '1234IsASecurePassword'

x = os.listdir('./Publish/badfiles')

for i in x:
    subprocess.call([
        'steghide',
        'extract',
        '-sf',
        f'./Publish/badfiles/{i}',
        '-p',
        password,
    ])

print(open('./SecretMessage.txt').read())       
```

The flag is:

```
DUCTF{m0r3_th4n_M33ts_th3_ey3}
```