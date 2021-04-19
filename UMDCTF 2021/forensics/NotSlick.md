# Not Slick - Forensics
Author - [BlackJack](http://github.com/Mannan-Goyal)
Requirements : Basic knowledge of Hex, the structure of png files and the magic number

---
When we start to solve the challenge we are faced with a problem description which says -

> My friend always messes with PNGs.... what did he do this time?

This gives us a pretty good idea about the png file being messed up

After this I open the png file with a normal image viewer just to confirm the fact.
Now I open the image with Bless Hex Editor, However u can use any hex editor of your choice. A list of popular hex editors can be found [here.](https://linuxhint.com/hex_editor_linux/)

The magic number for a png file : ```89 50 4E 47 .PNG```

A list of magic numbers for different file types can be found [here.](https://asecuritysite.com/forensics/magic)

After looking at the hex of the image
![Init Hex](https://i.imgur.com/5IdSmiT.png)

I saw that the initial hex didn't match the magic number of png so I edited it to that but that didn't work

Later, i realised when I scrolled to the bottom of the file
![End hex](https://i.imgur.com/xEewiKu.png)
that the PNG and IHDR is inverted and hence the whole file was actually inverted 

So we wrote a python script to re-invert the file
```python
f1 = open("notslick.png", "rb+")
f2 = open("out.png", "wb+")
f2.write(f1.read()[::-1])
f1.close()
f2.close()
```
(Credits: [UnknownAbyss](https://github.com/unknownabyss))

After this when you open the image you find the flag which is -
![flag](https://i.imgur.com/TOprNZ6.png)
(Disable Dark Mode to view image xD)

```UMDCTF-{abs01ute1y_r3v3r53d}```
