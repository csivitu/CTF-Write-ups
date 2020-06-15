def xor(str1, str2):
    return chr(ord(str1)^ord(str2))

flag = [None]*38
key = 'I_l0v3_r3v3r51ng'

ciphertext = open('snake.txt').read()

k = len(ciphertext) - (len(flag) - len(key)//2)

for i in range(len(key)//2, len(flag)):
    flag[i] = xor(key[i%16], ciphertext[k])
    k += 1

for i in range(len(flag)//3, len(flag)//3 * 2):
    flag[i] = chr((ord(ciphertext[i]) - i)//ord(key[i%len(key)]))


for i in range(len(flag)//3):
    flag[i] = chr((ord(ciphertext[i]) + i)//ord(key[i]))

print(''.join(flag))