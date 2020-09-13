from pwn import remote

l = []

def connect():
    r = remote('crypto.chal.csaw.io', 5001)

    print(r.recvuntil('\n').decode())

    return r


def send(r, x):
    r.sendline(x)
    print(x)


def run(r):
    x = r.clean()
    print(x)                     # Enter plaintext

    send(r, 'a' * 64)

    print(r.recvuntil('Ciphertext is:  '))
    x = r.recvline().decode()    # Ciphertext value
    print(x)

    if x[0:32] == x[32:64]:
        mode = 'ECB'
        l.append(0)
    else:
        mode = 'CBC'
        l.append(1)

    print(r.recvline())           # ECB or CBC

    send(r, mode)



def solve():
    r = connect()

    i = 0
    while True:
        try:
            run(r)
        except:
            print(i)
            print(r.recvall())
            print(l)
            exit(1)
        i+=1

    r.interactive()

solve()

'''
[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1]
'''