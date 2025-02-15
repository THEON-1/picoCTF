#!/usr/bin/env python3
from pwn import *
import matplotlib.pyplot as plt

address = "saturn.picoctf.net"
port = 63821

def fetch_data(message):
    conn = remote(address, port, level="warn")
    conn.recvuntil(b"hex: ")
    conn.sendline(message)
    conn.recvuntil(b"[")
    list_string = conn.recvuntil(b"]", drop=True)
    conn.close()
    return [int(s.strip()) for s in list_string.split(b',')]

data_array = []
P = log.progress("fetching timing data")
for i in range(16):
    P.status(f"{i+1}/16")
    data_array.append(fetch_data(b"00112233445566778899aabbccddeeff"))
P.success("16/16 all data fetched")

data = [0]*len(data_array[0])
for i in range(len(data_array)):
    slice = data_array[i]
    for j, n in enumerate(slice):
        data[j] += n

plt.plot(data)
plt.show()

