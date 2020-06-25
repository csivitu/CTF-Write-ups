from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}

num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}
ctxt = 'z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut'
pseudo_key = 'iigesssaemk'

def get_key(pkey):
    x = ''
    y = ''
    for i in range(len(pkey)):
        c = chr_to_num[pkey[i]]
        x += num_to_chr[c/2]
        y += num_to_chr[(c+26)/2]
    print(x)
    print(y)

get_key(pseudo_key)

key = 'redpwwwnctf'

def decrypt(ct, key):
    flag = ''
    key = ''.join(key[i % len(key)] for i in range(len(ct))).lower()
    for i in range(len(ct)):
        if ct[i] == '_':
            flag += '_'
            continue
        flag += num_to_chr[(chr_to_num[ct[i]] - chr_to_num[key[i]]) % 26]
    print(flag)
decrypt(ctxt, key)