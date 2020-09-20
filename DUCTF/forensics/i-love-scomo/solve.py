# Get ilovescomo.jpg.out using stegcrack
text = open('./ilovescomo.jpg.out', 'r').read().split('\n')

l = ['0'] * len(text)

for i in range(len(text)):
    if text[i] == '':
        continue
    if text[i][-1] == ' ':
        l[i] = '1'

print(''.join(l))

l = [chr(int(''.join(l[i:i+8]), 2)) for i in range(0, len(l), 8)]

print(''.join(l))