# Dora the explorer - OSINT

Author - [BlackJack](http://github.com/Mannan-Goyal)

Requirements : Know how to google, exiftool, XOR

* * *

When we start to solve the challenge we are faced with a pretty elaborate hint which says -

> Hi, I am Dora the Explorer and I love exploring as you know ;) (after all 1+1=0), and I recently found this place which has an a very cool looking street art to it. Plus they posted about it on social media many a times. You all should see this too sometime!!!

#### Also, we are provided with the following image -

<p align="center"><img src="https://imgur.com/42RvVoA.png" alt="Chall Image" height="400px"></p>


#### If you carefully look at the picture you'll see this -
<p align="center"><img align="center" alt="Challenge_Zommed_In" src="https://imgur.com/k12qN8F.png"></p>

- After seeing this my first instinct was to google social street. Among the many results I found this [instagram page](https://www.instagram.com/thesocialstreet_/?hl=en).

- After scrolling through a bit I realised that there was no street art or anything related to it, so I searched for social street on instagram search. The first result to come up was [this](https://www.instagram.com/socialstreetcafe/?hl=en).

- Scrolling a bit lead me to this [post.](https://www.instagram.com/p/CKGRq81l5bv/) This seemed like street art also.

- Upon opening this I found the comment by [@thevisheshbansal](https://www.instagram.com/thevisheshbansal/) saying

> I know you came a long way to find this. Here is a flag for you: 
```
j}mu?c:i=}Qf?j=Q:b>zQ}>Ql=Qm:|=h{?s
```

- Well the challenge is still not over, we need to decrypt the flag. During the ctf I visited [cyberchef](https://gchq.github.io/CyberChef/) put the flag as input and used the `magic mode` with `intensive setting` turned on cause I wanted to finish the chall fast.

![Magic_Decode](https://imgur.com/sYAqLzd.png)

- But from the hint `(1+1=0)` given in the challenge we could figure out that we might have to use XOR.

- And in the comment it was mentioned the key to unlock the flag is the device manufacturer of the image given initially.

- So running exiftool....
  
 <p align="center"><img alt="exiftool" src="https://imgur.com/37wsVWU.png"></p>
 
- Hence trying out XOR with key `OnePlus`
 ![XOR](https://imgur.com/CjuFOZG.png)
 
- So finally the flag is
`dsc{1m4g3s_h1d3_4l0t_s0_b3_c4r3fu1}`

