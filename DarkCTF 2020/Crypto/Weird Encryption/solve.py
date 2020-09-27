import string

prefix="Hello. Your flag is DarkCTF{"
suffix="}."
main_string="c an u br ea k th is we ir d en cr yp ti on".split()

flag = ''

clear_text = prefix + flag + suffix
enc_text = ""
for letter in clear_text:
    c1 = ord(letter) // 16
    c2 = ord(letter) % 16
    enc_text += main_string[c1]
    enc_text += main_string[c2]

encrypted = 'eawethkthcrthcrthonutiuckirthoniskisuucthththcrthanthisucthirisbruceaeathanisutheneabrkeaeathisenbrctheneacisirkonbristhwebranbrkkonbrisbranthypbrbrkonkirbrciskkoneatibrbrbrbrtheakonbrisbrckoneauisubrbreacthenkoneaypbrbrisyputi'

x = ''
a = []
i = 0

while i < len(encrypted):
    x += encrypted[i]
    if x in main_string:
        if x == 'c' and encrypted[i+1] == 'r':
            i += 1
            continue
        a.append(x)
        x = ''
    i += 1

def encrypt(letter):
    enc_text = ''
    c1 = ord(letter) // 16
    c2 = ord(letter) % 16
    enc_text += main_string[c1]
    enc_text += main_string[c2]
    return enc_text

d = {}

for i in (string.ascii_letters + '._{} @1234567890'):
    d[encrypt(i)] = i

a = [a[i] + a[i+1] for i in range(0, len(a) - 1, 2)]

for i in a:
    print(d.get(i), end='')
