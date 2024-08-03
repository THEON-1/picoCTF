#!python3
from sage.all import *
import pwn

conn = pwn.remote("jupiter.challenges.picoctf.org", 4557)

conn.recvuntil(b"c: ")
c = Integer(conn.recvline().strip())
pwn.log.info("c: 0x{:x}".format(c))

conn.recvuntil(b"n: ")
n = Integer(conn.recvline().strip())
pwn.log.info("n: 0x{:x}".format(n))

conn.recvuntil(b"e: ")
e = Integer(conn.recvline().strip())
pwn.log.info("e: 0x{:x}".format(e))

conn.close()

pwn.log.info("factoring n")
factors = factor(n)
pwn.success("factorization: {}".format(factors))

totient = prod([x[0]-1 for x in factors])
pwn.log.info("totient: {:x}".format(totient))

pwn.log.info("calculating d")
d = pow(e, -1, totient).lift()
pwn.log.success("d: {:x}".format(d))

m = pow(c, d, n).lift()
flag = pwn.pack(int(m), 'all', 'big', False)
pwn.log.info("flag: {}".format(flag))

