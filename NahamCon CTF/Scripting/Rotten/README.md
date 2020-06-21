# Rotten

Author: [roerohan](https://github.com/roerohan)

This is a scripting challenge based on the Caesar's Cipher. Upon connecting to the server using `netcat`, the server spits out a string, which may or may not contain a character of the flag in it. You have to decrypt the same string, and send it back to the server. This is repeated until the entire flag is obtained.

# Requirements

- Basic Knowledge of Caesar's Cipher
- Python 3

# Exploitation

```bash
$ nc jh2i.com 50034                       
send back this line exactly. no flag here, just filler.
```

When you `netcat` onto the server, it says `send back this line exactly. no flag here, just filler.`, which is basically exactly what you have to do.

> Note: The 2nd, 4th, etc. lines are the replies sent to the server.

```bash
$ nc jh2i.com 50034                           
send back this line exactly. no flag here, just filler.
send back this line exactly. no flag here, just filler.
zluk ihjr aopz spul lehjasf. uv mshn olyl, qbza mpssly.
send back this line exactly. no flag here, just filler.
```

As you see, the second time, the server sends a message encrypted using Caesar's cipher. In this cipher, every character in the message is shifted by an offset. So, if the offset is 2, 'a' becomes 'c', 'b' becomes 'd', and so on...
<br />

Everytime the server sends an encrypted message, you have to find out the decrypted message and send it back to the server. Normally, you might have to bruteforce the offset for the cipher. But, after 3-4 messages, you see that the first part of the message, i.e, `send back this line exactly.`, is always the same. This can be used to calculate the offset.
<br />

Here's an example of the other type reply the server might.

```
vhqg edfn wklv olqh hadfwob. fkdudfwhu 10 ri wkh iodj lv 'r'
send back this line exactly. character 10 of the flag is 'o'
```

Since the first part is always the same, you can easily calculate the offset (count the number of letters between v and s).
<br />

Of course, there's a reason this is a 'scripting' challenge. The server will keep sending random characters from the flag, in this fashion. So, it is not a good idea to manually map the characters in all positions. Time to fire up python and write a script.
<br />

```python
flag = {}

def flagify(flag):
    f = [None]*40
    for i in flag:
        f[i] = flag[i]
    f = [i for i in f if i != None]
    return ''.join(f)

def reply(recv):
    global flag
    m = 'send back this line exactly. no flag here, just filler.'
    l = len(m)

    if len(recv)==l:
        return m
    else:
        diff = ord(recv[0])-ord('s')
        if (diff < 0): diff +=26
        c = ''
        x = -1
        for i in recv:
            if i == ' ' or i == '\'' or i == '.' or i == '{' or i == '}' or i =='_':
                c += i
            elif i.isnumeric():
                c += i
                if x == -1: x = int(i)
                else: x = x*10 + int(i)
            elif ord(i) - diff < ord('a'):
                c += chr(ord(i) - diff + 26)
            else:
                c += chr(ord(i) - diff)

        if x != -1:
            flag[x] = c[-2]
        return c

from pwn import remote

r = remote('jh2i.com', 50034)

while True:
    rec = r.recv()
    if rec:
        rec = str(rec)[2:-3]
        print(rec)
        t = reply(rec)
        r.send(t)
        print(t)
        print(flagify(flag))
```

> Note: This is not the most efficient, well-written code, because it doesn't need to be.

We're using the `pwntools` library for the remote `netcat` connection. The idea is to extract out the character from the message and store it in a dictionary along with it's index, in the format:

```python
{
    'index': 'character',
}
```

The flagify function takes this flag dictionary and returns a string, after mapping every character to the correct index.
<br />

The reply function is actually decoding the cipher. If the length of the message is the same as `send back this line exactly. no flag here, just filler.`, it just returns that string. If not, it calculates the offset from the first character of the server message. Then it uses that offset to decrypt every other character. During the decryption, it stores the index and the corresponding character in the dictionary.
<br />

The last part of the program is just for connecting to `netcat`, and sending and receiving messages.
<br />

As you run the script, you'll see a 31 character string form on your terminal over 45-60 seconds (varies based on how lucky you are). That is the final flag. Here's a sample:

```
$ python flag.py
[+] Opening connection to jh2i.com on port 50034: Done
send back this line exactly. no flag here, just filler.
send back this line exactly. no flag here, just filler.

xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 29 tk ymj kqfl nx 'x'
send back this line exactly. character 29 of the flag is 's'
s
kwfv tsuc lzak dafw wpsuldq. uzsjsulwj 14 gx lzw xdsy ak 'f'
send back this line exactly. character 14 of the flag is 'n'
ns
fraq onpx guvf yvar rknpgyl. punenpgre 1 bs gur synt vf 'y'
send back this line exactly. character 1 of the flag is 'l'
lns
.
.
.
kwfv tsuc lzak dafw wpsuldq. fg xdsy zwjw, bmkl xaddwj.
send back this line exactly. no flag here, just filler.
flag{now_you_know_your_caesars}
bnwm kjlt cqrb urwn ngjlcuh. wx oujp qnan, sdbc oruuna.
send back this line exactly. no flag here, just filler.
flag{now_you_know_your_caesars}
pbka yxzh qefp ifkb buxzqiv. zexoxzqbo 1 lc qeb cixd fp 'i'
send back this line exactly. character 1 of the flag is 'l'
flag{now_you_know_your_caesars}
```

Once you obtain this string, you can stop execution. The flag is `flag{now_you_know_your_caesars}`.
<br />

P.S.: Here's some code that might be a little better:

```python
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
```

The flag is:

```
flag{now_you_know_your_caesars}
```