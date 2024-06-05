#!/usr/bin/python

with open("enc", "r") as f:
    while True:
        char = f.read(1)
        if not char:
            break
        c = ord(char)
        char_1 = chr(c >> 8)
        char_2 = chr(c%(2**8))
        print(char_1, end='')
        print(char_2, end='')

print('\n')

