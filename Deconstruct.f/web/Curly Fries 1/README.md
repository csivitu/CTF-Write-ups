# Curly Fries 1 - Web

Author - [UnknownAbyss](https://github.com/UnknownAbyss)

Requirements : cURL

* * *

The challenge gives us the following text -

> Normal fries are nice, but everything's better with a curl in it. The flag is right in front of you.


```
very.uniquename.xyz:8880
```

#### Upon opening the link we see -

<p align="center"><img src="https://i.imgur.com/pa1MPge.png" alt="Chall Image"></p>

This screams sweden. So we try to set the language headers to swedish

```sh
curl -H "Accept-Language: sv-SE" very.uniquename.xyz:8880
```

This gives us the flag...
```
dsc{1_l0v3_sw3d3n}
```
