#!/home/maxime/.pyvenv/bin/python3
import string

ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
    dec = ''
    assert len(enc) % 2 == 0
    for i in range(0, len(enc), 2):
        char = 0
        msb = ord(enc[i]) - ord('a')
        lsb = ord(enc[i+1]) - ord('a')
        char += (msb << 4) + lsb
        dec += chr(char)
    return dec

def decode(c, k):
    t1 = ord(c) - ord('a')
    t2 = ord(k) - ord('a')
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

with open("string", 'r') as f:
    text = f.read().strip()
    keyset = ALPHABET
    for key in keyset:
        decrypted = ''
        for char in text:
            decrypted += decode(char, key)
        print(b16_decode(decrypted))

