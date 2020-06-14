# Agent 95

Author: [roerohan](https://github.com/roerohan)

As the name suggest, change the User Agent to Windows 95.

# Requirements

- Basic Knowledge of Request headers

# Source

- http://jh2i.com:50000.

```
They've given you a number, and taken away your name~

Connect here:
http://jh2i.com:50000
```

# Exploitation

The challenge is very simple once you know what to do. 

```
We will only give our flag to our Agent 95! He is still running an old version of Windows...
```

We assume Agent 95 uses Windows 95. So just change the `User-Agent` header to `Mozilla/4.0 (compatible; MSIE 4.01; Windows 95)`.

```python
>>> import requests
>>> r = requests.get('http://jh2i.com:50000', headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 4.01; Windows 95)'})
>>> r.text
'flag{user_agents_undercover}\n<div style="text-align:center">\n<br><br><br><br>\n<b> NOT CHALLENGE RELATED:</b><br>THANK YOU to Digital Ocean for supporting NahamCon and NahamCon CTF!\n<p>\n<img width=600px src="https://d24wuq6o951i2g.cloudfront.net/img/events/id/457/457748121/assets/1b5a9739fd31b42fa4eb37ac6b3a6e1c.DOlogo.png">\n</p>\n</div>'
```

There, you got the flag.

```
flag{user_agents_undercover}
```