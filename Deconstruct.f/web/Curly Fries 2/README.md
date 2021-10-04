# Curly Fries 2 - Web

Author - [UnknownAbyss](https://github.com/UnknownAbyss)

Requirements : cURL

* * *

The challenge gives us the following text -

> Normal fries are nice, but everything's better with a curl in it. Why do logos make things so recognizable?


```
very.uniquename.xyz:2052    
```

#### Upon opening the link we see -

<p align="center"><img src="https://i.imgur.com/h0cj6FI.png" alt="Chall Image"></p>

We see the logo of xbox and linux on the screen. This is me accessing this page on a windows device

Putting User-Agent as Linux...

```sh
curl -H "User-Agent: Linux" very.uniquename.xyz:2052
```

...we get this back

```html
...
<body>
<article class="xbox"><img src="https://compass-ssl.xbox.com/assets/f8/17/f817aa8c-02c1-4ba9-84a8-20d357d52939.jpg?n=Microsoft-Store-2018_Feature-0_Pay_1040x585.jpg" alt="Xbox"></article>
</body>
...
```

We see the linux logo is gone. Hence we put user agent as both Linux and Xbox

```sh
curl -H "User-Agent: Linux Xbox" very.uniquename.xyz:2052
```

This gives us the flag inside the body of the page...
```
dsc{1m4g1n3_l1nux_0n_4n_xb0x}
```
