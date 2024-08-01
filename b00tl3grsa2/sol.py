#!python3
from pwn import *

conn = remote("jupiter.challenges.picoctf.org", 19566)

conn.recvuntil(b"c: ")
c = int(conn.recvline().strip())
log.info("c: {:x}".format(c))

conn.recvuntil(b"n: ")
n = int(conn.recvline().strip())
log.info("n: {:x}".format(n))

conn.recvuntil(b"e: ")
e = int(conn.recvline().strip())
log.info("e: {:x}".format(e))

m = pow(c, 65537, n)
m_literal = pack(m, 'all', 'big', False)
log.success("flag: {}".format(m_literal))

