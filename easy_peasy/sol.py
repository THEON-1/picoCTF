#!/home/maxime/.pyvenv/bin/python3
from pwn import *
import binascii

buffersize = 50000-32

conn = remote("mercury.picoctf.net", 36981)
conn.recvline()
conn.recvline()

encrypted_flag = conn.recvline().strip()

conn.recvuntil(b'?')

conn.sendline(b'0' * buffersize)

conn.recvuntil(b'?')

conn.sendline(b'0' * 32)

conn.recvline()

encrypted_0s = conn.recvline().strip()

conn.close()

encrypted_flag = binascii.unhexlify(encrypted_flag)
encrypted_0s = binascii.unhexlify(encrypted_0s)
for i in range(32):
    print(chr(encrypted_0s[i] ^ encrypted_flag[i] ^ ord('0')), end='')
print()

