#!/home/maxime/.pyvenv/bin/python3
from pwn import *

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

with open("ciphertext", 'r') as f:
    ciphertext = f.read()

out = ""
prev = 0
for char in ciphertext:
    pos = lookup2.index(char)
    out += lookup1[(pos+prev)%40]
    prev = (pos+prev)%40

print(out)


