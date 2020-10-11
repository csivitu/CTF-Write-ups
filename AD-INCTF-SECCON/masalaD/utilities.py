from pwn import remote
import time
import re
import os

def extract_flag(text):
    return re.findall(r'bi0s\{\w{26}\}', text)

def submit_flag(flag, host='10.40.0.2', port=5555):
    if isinstance(flag, list):
        flag = '\n'.join(flag)

    print(f'[INFO] Submitting flag {flag} to {host}:{port}.')

    r = remote(host, port)
    r.sendline(flag)
    
    if '\n' in flag:
        for _ in range(len(flag.split('\n'))):
            print(r.recvline())
    else:
        print(r.recvline())

    r.close()

