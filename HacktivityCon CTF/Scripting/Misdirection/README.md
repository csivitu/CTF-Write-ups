# Misdirection

Author: [roerohan](https://github.com/roerohan)

# Requirements

- Python

# Source

```
Check out the new Flag Finder service! We will find the flag for you!

Connect here:
http://jh2i.com:50011/
```

# Exploitation

Here, every other site you visit gives you an additional character of the flag, and redirects you to a new site.

```python
import requests

host = "http://jh2i.com:50011"
default = host + "/site/flag.php"

r = requests.get(default, allow_redirects=False)

flag = ''

while not flag or flag[len(flag)-1] != '}':
    r = requests.get(host + r.headers["Location"], allow_redirects=False)

    if (int(r.headers['Content-Length']) > 0):
        flag += r.text.split('flag is ')[1].strip()
    print(flag)
```

Run this and you get the flag, letter by letter.

```bash
$ python script.py 

f
f
fl
fl
fla
fla
flag
flag
flag{
flag{
flag{h
flag{h
flag{ht
flag{ht
flag{htt
flag{htt
flag{http
flag{http
flag{http_
flag{http_
flag{http_3
flag{http_3
flag{http_30
flag{http_30
flag{http_302
flag{http_302
flag{http_302_
flag{http_302_
flag{http_302_p
flag{http_302_p
flag{http_302_po
flag{http_302_po
flag{http_302_poi
flag{http_302_poi
flag{http_302_poin
flag{http_302_poin
flag{http_302_point
flag{http_302_point
flag{http_302_point_
flag{http_302_point_
flag{http_302_point_y
flag{http_302_point_y
flag{http_302_point_yo
flag{http_302_point_yo
flag{http_302_point_you
flag{http_302_point_you
flag{http_302_point_you_
flag{http_302_point_you_
flag{http_302_point_you_i
flag{http_302_point_you_i
flag{http_302_point_you_in
flag{http_302_point_you_in
flag{http_302_point_you_in_
flag{http_302_point_you_in_
flag{http_302_point_you_in_t
flag{http_302_point_you_in_t
flag{http_302_point_you_in_th
flag{http_302_point_you_in_th
flag{http_302_point_you_in_the
flag{http_302_point_you_in_the
flag{http_302_point_you_in_the_
flag{http_302_point_you_in_the_
flag{http_302_point_you_in_the_r
flag{http_302_point_you_in_the_r
flag{http_302_point_you_in_the_ri
flag{http_302_point_you_in_the_ri
flag{http_302_point_you_in_the_rig
flag{http_302_point_you_in_the_rig
flag{http_302_point_you_in_the_righ
flag{http_302_point_you_in_the_righ
flag{http_302_point_you_in_the_right
flag{http_302_point_you_in_the_right
flag{http_302_point_you_in_the_right_
flag{http_302_point_you_in_the_right_
flag{http_302_point_you_in_the_right_r
flag{http_302_point_you_in_the_right_r
flag{http_302_point_you_in_the_right_re
flag{http_302_point_you_in_the_right_re
flag{http_302_point_you_in_the_right_red
flag{http_302_point_you_in_the_right_red
flag{http_302_point_you_in_the_right_redi
flag{http_302_point_you_in_the_right_redi
flag{http_302_point_you_in_the_right_redir
flag{http_302_point_you_in_the_right_redir
flag{http_302_point_you_in_the_right_redire
flag{http_302_point_you_in_the_right_redire
flag{http_302_point_you_in_the_right_redirec
flag{http_302_point_you_in_the_right_redirec
flag{http_302_point_you_in_the_right_redirect
flag{http_302_point_you_in_the_right_redirect
flag{http_302_point_you_in_the_right_redirecti
flag{http_302_point_you_in_the_right_redirecti
flag{http_302_point_you_in_the_right_redirectio
flag{http_302_point_you_in_the_right_redirectio
flag{http_302_point_you_in_the_right_redirection
flag{http_302_point_you_in_the_right_redirection
flag{http_302_point_you_in_the_right_redirection}
````

The flag is:

```
flag{http_302_point_you_in_the_right_redirection}
```