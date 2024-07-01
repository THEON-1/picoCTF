#!/home/maxime/.pyvenv/bin/python3
from pwn import *

with open("enc_flag", 'r') as f:
    text = f.readlines()
    a = int(text[0][4:].strip())
    b = int(text[1][4:].strip())
    cipher = text[2][11:].replace('[', '').replace(']', '').replace(' ', '').strip().split(',')
    
    p = 97
    g = 31
    text_key = "trudeau"

    key = pow(g, a*b, p)
    semi_cipher = ""
    for i in cipher:
        i = int(i.strip())
        semi_cipher += chr(i // (311*key))
    plaintext = ""
    for i, char in enumerate(semi_cipher):
        plaintext += chr(ord(char) ^ ord(text_key[i%len(text_key)]))
    plaintext = plaintext[::-1]
    print(plaintext)

