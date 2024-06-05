#!/usr/bin/python

def rot13(char):
    c = ord(char)
    A = ord('A')
    Z = ord('Z')
    a = ord('a')
    z = ord('z')
    if c >= A and c <= Z:
        char = chr((c-A+13)%(Z-A+1)+A)
    elif c >= a and c <= z:
        char = chr((c-a+13)%(z-a+1)+a)
    print(char, end='')

with open("flag", "r") as f:
    flag = f.read()
    for char in flag:
        rot13(char)

