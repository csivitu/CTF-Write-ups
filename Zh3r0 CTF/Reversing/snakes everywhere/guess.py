flag = 'zh3ro{fake flag}'
key = 'I_l0v3_r3v3r51ng'

# flag size is 38

def xor(str1, str2):
    return chr(ord(str1)^ord(str2))

ciphertext = ''

for i in range(len(flag)//3):
    ciphertext += chr(ord(key[i]) * ord(flag[i]) - i)


for i in range(len(flag)//3, len(flag)//3 * 2):
    ciphertext += chr( ord(flag[i]) * ord(key[i%len(key)]) + i)

for i in range(len(key)//2, len(flag)):
    ciphertext += xor(key[i%16], flag[i])

file = open('ciphertext.txt', 'w')
print(len(ciphertext))

file.write(ciphertext)
file.close()
