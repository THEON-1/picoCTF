#!/home/maxime/.pyvenv/bin/python3

def decode(char):
    char = ord(char)
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')

    if a <= char and char <= z:
        return chr(z - (char - a))
    if A <= char and char <= Z:
        return chr(Z - (char - A))
    return chr(char)

with open("encrypted.txt", 'r') as f:
    text = f.read()
    dec = ''.join(map(decode, text))
    print(dec)

