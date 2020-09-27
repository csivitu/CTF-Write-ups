# E-AES

Author: [roerohan](https://github.com/roerohan)

## Source

```
55 2b 31 46 36 34 33 55 2b 31 46 34 42 35 55 2b 31 46 33 33 46 55 2b 31 46 33 41 34 55 2b 31 46 36 41 41 55 2b 31 46 33 30 46 55 2b 31 46 34 30 45 55 2b 31 46 39 34 42 55 2b 31 46 36 41 42 55 2b 31 46 36 30 36 55 2b 31 46 35 32 41 55 2b 31 46 35 32 43 55 2b 31 46 36 41 41 55 2b 32 37 35 33 55 2b 31 46 36 30 37 55 2b 31 46 36 30 36 55 2b 31 46 33 37 34 55 2b 31 46 34 30 44 55 2b 31 46 33 34 43 55 2b 31 46 33 41 34 55 2b 31 46 33 32 41 55 2b 31 46 33 37 34 55 2b 32 36 30 30 55 2b 31 46 36 41 38 55 2b 31 46 34 45 45 55 2b 31 46 36 30 44 55 2b 32 37 30 35 55 2b 31 46 33 43 45 55 2b 31 46 34 41 37 55 2b 31 46 36 42 39 55 2b 31 46 33 30 39 55 2b 31 46 35 32 43 55 2b 32 37 35 33 55 2b 31 46 36 42 39 55 2b 31 46 35 39 30 55 2b 31 46 39 32 33 55 2b 31 46 36 30 36 55 2b 31 46 39 32 33 55 2b 31 46 36 41 38 55 2b 32 33 32 38 55 2b 31 46 36 30 44 55 2b 31 46 36 41 41 55 2b 31 46 33 46 39 55 2b 31 46 35 37 39 55 2b 31 46 36 30 44 55 2b 31 46 33 41 34 55 2b 31 46 33 38 38 55 2b 31 46 33 34 43 55 2b 31 46 39 39 33 55 2b 32 37 35 33 55 2b 31 46 36 30 30 55 2b 32 37 35 33 55 2b 32 36 30 33 55 2b 31 46 33 43 45 55 2b 32 36 30 30 55 2b 32 36 30 32 55 2b 32 37 30 35 55 2b 31 46 36 30 31 55 2b 31 46 33 38 38 55 2b 31 46 34 45 45 55 2b 31 46 36 30 41 55 2b 32 37 31 36 55 2b 31 46 36 41 42 55 2b 32 31 33 39
```

## Exploit

The numbers are actually Unicode characters in hex. Convert them to Unicode, and you get a list of emojis. Now convert this Unicode string to base64 and you get:

```
U2FsdGVkX1/SdY61KvbsHKyLM9+cwmnSYmh313LQ9dAN9sBbzYgYIcyu+0BM5xXi
```

Since we do not know the AES key, we can have a simple shell script to bruteforce the key with `rockyou.txt`.

```sh
echo "Start!"
while read p; do
  # Emojis in base64
  printf "U2FsdGVkX1/SdY61KvbsHKyLM9+cwmnSYmh313LQ9dAN9sBbzYgYIcyu+0BM5xXi" | openssl enc -d -base64 -A -aes-256-cbc -md md5 -pass pass:"$p" >> logs.txt 2>>logs.txt
done <rockyou.txt

# darkCTF{3ur3k4!_1t'5_3m0j1_43s}
```

The flag is:

```
darkCTF{3ur3k4!_1t'5_3m0j1_43s}
```