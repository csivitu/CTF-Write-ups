import requests
import base64

local = False

url = lambda x: "http://crypto.chal.csaw.io:5003" + x

if local:
    url = lambda x: "http://localhost:5000" + x


def view(id, integrity):
    print(f"\n\nSending id={id}, integrity={integrity}\n\n")
    r = requests.post(
        url("/view"),
        data={
            "id": id,
            "integrity": integrity,
        },
    )

    print("\n\n")
    print(r.text)
    return r.text


data = {
    "entrynum": 7,
    "author": "&admin=True",
    "note": "&access_sensitive=True&entrynum=7",
}

r = requests.post(url("/new"), data=data)

encoded, hexdigest = r.text.strip().split(":")
encoded = encoded.split('Successfully added ')[1]

print("Encoded: " + encoded)
print("Hexdigest: " + hexdigest)

flag = view(encoded, hexdigest)

'''
flag{h4ck_th3_h4sh}
'''