# Pickle Rick - Stegnography
Author - [BlackJack](http://github.com/Mannan-Goyal)

Requirements : binwalk, steghide or not

---
When we start to solve the challenge we are faced with a problem description which says -

> You recieve these audio files from someone named Alan Eliasen.

After reading this statement we get 2 key hints, one that we have to find hidden messages in audio files and a name - Alan Eliasen.

If you google the name you'll reach [here.](https://futureboy.us/)

Here given the category of the challenge we select Stegnography and then Decode an Image to reach [here.](https://futureboy.us/stegano/)

![Upload](https://i.imgur.com/m3xP0kS.png)

After this we uploaded the ```together-forever-encoded.wav``` file in the decoder, we get the following string displayed -

```The password is "big_chungus"!```

Now we upload the 2nd file to the website but this time instead of leaving the password field empty we put big_chungus there.

The following is obtained- 
```UMDCTF-{n3v3r_g0nna_l3t_y0u_d0wn}```
which is the required flag.

The above method was suggested later by [Rakesh](https://github.com/Rakesh1772) but to solve the challenge earlier I had used steghide, the commands I ran are listed below

```bash
steghide extract -sf together-forever-encoded.wav
steghide extract -sf rickroll.wav
```
