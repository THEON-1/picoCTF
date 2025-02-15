#!/usr/bin/env python3
from pwn import *

with open("challengefile", "rb") as f:
    file = f.read()

log.info(f"length: {len(file)}")

reorder = b""

for i in range(len(file)//4):
    reorder += file[i+3:i+4] + file[i+2:i+3] + file[i+1:i+2] + file[i:i+1]

log.hexdump(reorder)

