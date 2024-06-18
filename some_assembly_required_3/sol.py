#!/home/maxime/.pyvenv/bin/python3

S = b'\x9dn\x93\xc8\xb2\xb9A\x8b\x94\xc6\xdf3\xc0\xc5\x95\xde7\xc3\x9f\x93\xdf?\xc9\xc3\xc2\x8c2\x93\x90\xc1\x8ee\x95\x9f\xc2\x8c6\xc8\x95\xc0\x90\x00\x00'
s = b'\xf1\xa7\xf0\x07\xed'
p = "picoCTF{"

for i, char in enumerate(S):
    key = s[4-(i%5)]
    if key // 128 > 0:
        key |= 0xffffff00
        char ^= key
        #print(bin((char ^ 0xffffffff) + 1))
        print(chr(char ^ 0xffffff00), end='')
    else:
        char ^= key
        #print(bin(char))
        print(chr(char), end='')

