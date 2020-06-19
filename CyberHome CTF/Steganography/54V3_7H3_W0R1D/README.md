# 54V3_7H3_W0R1D

Author: [roerohan](https://github.com/roerohan)

This is a steganography challenge with multiple steps to follow.

# Requirements

- `file` command
- binwalk
- john (John the Ripper)
- pngcheck
- `strings` command

# Source

- https://mega.nz/file/FvpFSQyT#x42nKDHgQm8_SBJsa8pN2ooA-YuusapfrDz9TbQGNK8
- [flag.ico](./flag.ico)

# Exploitation

You are given a `flag.ico` file. But when you run `file` on that, you see:

```bash
$ file flag.ico 
flag.ico: MS Windows icon resource - 1 icon, 256x256 with PNG image data, 256 x 256, 8-bit/color RGBA, non-interlaced, 32 bits/pixel
```

So it's a PNG file, but it's rather big, about 5MB. So, we can run `binwalk` on it to see if there are any files hidden here. 

```bash
$ binwalk -e flag.ico 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
22            0x16            PNG image, 256 x 256, 8-bit/color RGBA, non-interlaced
63            0x3F            Zlib compressed data, best compression

WARNING: Extractor.execute failed to run external extractor '7z x -y '%e' -p ''': [Errno 2] No such file or directory: '7z', '7z x -y '%e' -p ''' might not be i
nstalled correctly
4513067       0x44DD2B        Zip archive data, encrypted at least v2.0 to extract, compressed size: 524662, uncompressed size: 525092, name: share.png
5037897       0x4CDF49        End of Zip archive, footer length: 22
```

So, in the extracted directory, we get a `44DD2B.zip` file, which is password protected. So, we can use John the Ripper to bruteforce it and break the password. Before that, we need to convert this to a format that `john` can read.

```bash
$ zip2john 44D2B.zip > 44D
```

Now we can pass this `44D` file to `john`, to bruteforce the password.

```bash
$ john 44D
```

This runs for a few seconds and returns the password, which is `sarah`. Now we can unzip the file and view it's contents. We get a file called `share.png`, which is an image. When you run `pngcheck` on it, you see that there is a strings after `IEND`. So, we get that string using `strings`.

```bash
$ strings share.png
...
IEND
iisiiiisiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiodoiiiiiiiiiiiiiiiioddddddddddoiiiiiiiiiiiiiiiiiiioddddddddddddddddddddddddddddddddddodddddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiiiioddddddddddddddddddddddddddddddddddddddddddodoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiodddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiodddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddodddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddoddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiio
```

Now, all we have to do is figure out what this string is. After a bit of research, you find out that it's actually an esoteric language called `deadfish` (also referred to as the deadfish cipher). You can now decode this online using `https://www.dcode.fr/deadfish-language`. Here you get the flag. The flag is:

```
cbrh{Y0U_54V3D_7H3_W0RLD}
```
