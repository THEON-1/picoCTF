#!/usr/bin/python

with open("data", 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = int(line.strip(), 16)
        for _ in range(4):
            print(chr(value%256), end='')
            value >>= 8

