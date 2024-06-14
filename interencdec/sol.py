#!/home/maxime/.pyvenv/bin/python3
from base64 import b64decode

def rot(n, s):
    a = ord('a')
    A = ord('A')
    z = ord('z')
    Z = ord('Z')
    S = ''
    for char in s:
        ochar = ord(char)
        if a <= ochar and ochar <= z:
            char = chr(((ochar - a + n) % 26) + a)
        elif A <= ochar and ochar <= Z:
            char = chr(((ochar - A + n) % 26) + A)
        S += char
    return S

with open("enc_flag", 'r') as f:
    enc_flag = f.read()
    dec1 = rot(19, b64decode(b64decode(enc_flag).strip().decode().replace('\'', '')[1:]).decode())
    print(dec1)

