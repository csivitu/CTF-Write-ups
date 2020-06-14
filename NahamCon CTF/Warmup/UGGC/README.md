# UGGC

Author: [roerohan](https://github.com/roerohan)

In this challenge, the goal is to modify the cookies so that you become the admin.

# Requirements

- Chrome Devtools

# Source

- http://jh2i.com:50018/login

```
Become the admin!

Connect here:
http://jh2i.com:50018
```

# Exploitation

When you type in a random username, for example, `csictf`, and check the Cookies in the Application tab of Chrome Dev-Tools (alternatively `console.log(document.cookie)`), you see a cookie named user set to `pfvpgs`. The target is to make the username corresponding to this cookie be `admin`. This is similar to another Caesar's cipher challenge.

As you see, there is an offset of 13 between the characters in `csictf` and `pfvpgs`. Therefore, you can find out the string corresponding to `admin` by encrypting it with an offset of 13.

```python
>>> print(''.join([chr((ord(i) + 13)) for i in 'admin']))
'nqzv{'
```

Now, the last character is `{`, so we subtract 26 to get the required character.

> Note: The offset is 13 and we know 'n' maps to 'a', so obviously 'a' will map to 'n', but we'll try it anyway.

```python
>>> print(chr(ord('{')-26))
'a'
```

So the target cookie is `nqzva`. Modify the cookie on Chrome Dev-tools and refresh the page to get the flag.

```
flag{H4cK_aLL_7H3_C0okI3s}
```