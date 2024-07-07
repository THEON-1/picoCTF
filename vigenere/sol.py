#!/home/maxime/.pyvenv/bin/python3

key = "CYLAB"

with open("cipher.txt", 'r') as f:
    cipher = f.read()
    
    plaintext = ""
    i = 0
    for char in cipher:
        char = ord(char)
        a = ord('a')
        z = ord('z')
        A = ord('A')
        Z = ord('Z')
        keychar = ord(key[i%len(key)]) - A
        if a <= char and char <= z:
            plaintext += chr((char - a - keychar)%26 + a)
            i += 1
        elif A <= char and char <= Z:
            plaintext += chr((char - A - keychar)%26 + A)
            i += 1
        else:
            plaintext += chr(char)
    print(plaintext)

