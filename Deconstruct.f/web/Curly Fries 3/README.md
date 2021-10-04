# Curly Fries 3 - Web

Author - [BlackJack](http://github.com/Mannan-Goyal)

Requirements : cURL, Network Headers and HTTP Methods

* * *

When we start to solve the challenge we are faced with a hint and a link -

> Normal fries are nice, but everything's better with a curl in it. I'm with you, every step of the way.


```
overly.uniquename.xyz:2095
```

#### Upon opening the link we see -

<p align="center"><img src="https://imgur.com/0RwPl3k.png" alt="Chall Image"></p>

So we try changing the Method to POST instead of GET whilst using cURL

```sh
curl -i -X POST http://overly.uniquename.xyz:2095/
```

In response we get -
```
perhaps try Googling me instead?
```

After seeing this, the initial thoughts were to visit the page as a Google bot, hence we tried to change the `User-Agent` header to that of a chrome crawler
```
curl -i -X POST -H "User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" http://overly.uniquename.xyz:2095/
```

After trying many variations of the above, we tried to set the Referer as google.com

```sh
curl -i -X POST -H "Referer: https://www.google.com" http://overly.uniquename.xy
z:2095/
```

which returned -
```
did you attend that lovely dinner party Hosted by dscvit?
```

This was pretty clear we need to set the host as dscvit.com

```sh
curl -i -X POST -H "Referer: https://www.google.com" -H "Host: https://www.dscvit.com" http://overly.uniquename.xyz:2095/
```

which returned -
```
potates and carrots are my friends, milk and Cookies will be my end
```

This is where we were stuck for hours, it was obvious that we needed to set the cookie as something but after trying from bugs bunny other cartoon charachters and giving up several times, we tried `user=root` cause potato and carrots are root vegetables. However, what was the use of milk there? I am clueless!

```
curl -i -X POST -H "Referer: https://www.google.com" -H "Host: https://www.dscvit.com" --cookie "user=root" http://overly.uniquename.xyz:2095/
```

which returns -
```
JFATHER, JMOTHER, JDAUGHTER, ____?
```
This is also a pretty obvious hint we need to set Content-Type as JSON

```
curl -i -X POST -H "Referer: https://www.google.com" -H "Host: https://www.dscvit.com" -H "Content-Type: application/json" --cookie "user=root" http://overly.uniquename.xyz:2095/
```

which returned -
```
{'error': 'json data missing'}
```

Therefore adding data to the request-
```
curl -i -X POST -H "Referer: https://www.google.com" -H "Host: https://www.dscvit.com" -H "Content-Type: application/json" --cookie "user=root" -d '{"foo":"bar"}' http://overly.uniquename.xyz:2095/
```

which returned -
```
{'error': {'messi': 'required'}}
```

Therefore adding messi to JSON-
```
curl -i -X POST -H "Referer: https://www.google.com" -H "Host: https://www.dscvit.com" -H "Content-Type: application/json" --cookie "user=root" -d '{"messi":"bar"}' http://overly.uniquename.xyz:2095/
```
which returned -
```
{'error': {'messi': 'which club am i at?'}}
```

Therefore adding PSG to JSON-
```
curl -i -X POST -H "Referer: https://www.google.com" -H "Host: https://www.dscvit.com" -H "Content-Type: application/json" --cookie "user=root" -d '{"messi":"psg"}' http://overly.uniquename.xyz:2095/
```

which returned -
```
Congrats! The flag is dsc{th15_15_w4y_t00_much_w0rk}
```
Yes it is too much work xD
 
- So finally the flag is
`dsc{th15_15_w4y_t00_much_w0rk}`
