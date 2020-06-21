flag = [None]*100
def response(s): 
    offset = ord(s[0]) - ord('s')

    position = 0

    res = ''
    for i in s:
        if not i.isalpha():
            if i.isnumeric():
                position = position*10 + int(i)

            res += i
            continue
        res += chr((ord(i) - ord('a') - offset) % 26 + ord('a'))

    if len(res) == 55:
        return res
    
    flag[position] = res[-2]

    return res

from pwn import remote

r = remote('jh2i.com', 50034)

while True:
    received = r.recv()
    x = received.decode().strip()

    print(x)
    y = response(x)
    r.send(y)    
    print(y)
    print()
    f = ''.join([i for i in flag if i != None])
    print(f)
    print()

# Rotten
