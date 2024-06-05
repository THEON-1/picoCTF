#!/usr/bin/python

with open("nc_out", "r") as f:
    lines = f.readlines()
    for line in lines:
        char = chr(int(line))
        print(char, end='')

