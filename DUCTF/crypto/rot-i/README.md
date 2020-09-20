# rot-i

Author: [roerohan](https://github.com/roerohan)

## Source

```
ROT13 is boring!
```

```
Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj :).
```

## Exploit

The shift offset increments by 1.

```py
text = "IAJBO{ndldie_al_aqk_jjrnsxee}"

offset = ord('I') - ord('D')

for i in text.lower():
    if not i.isalpha():
        print(i, end = '')
    else:
        print(chr((ord(i) - offset - ord('a')) % 26 + ord('a')), end = '')
    offset += 1
```

The flag is:

```
DUCTF{crypto_is_fun_kjqlptzy}
```