#!python3
from sage.all import *
import pwn

pwn.log.info("reading file")
with open("public-key.txt", 'r') as f:
    lines = f.readlines()
    n1 = Integer(lines[0][4:].strip())
    n2 = Integer(lines[1][4:].strip())
    n3 = Integer(lines[2][4:].strip())
    e = Integer(lines[3][3:].strip())
    c = Integer(lines[4][3:].strip())

pwn.log.info("calculating p, q, r")
p = gcd(n1, n2)
q = gcd(n1, n3)
r = gcd(n2, n3)
assert p*q == n1
assert p*r == n2
assert q*r == n3
pwn.success("p: {:x}".format(p))
pwn.success("q: {:x}".format(q))
pwn.success("r: {:x}".format(r))

pwn.log.info("calculating d1, d2, d3")
_p = p-1
_q = q-1
_r = r-1
d1 = pow(e, -1, _p*_q).lift()
d2 = pow(e, -1, _p*_r).lift()
d3 = pow(e, -1, _q*_r).lift()
pwn.log.success("d1: {:x}".format(d1))
pwn.log.success("d2: {:x}".format(d2))
pwn.log.success("d3: {:x}".format(d3))

pwn.log.info("decrypting message...")
m2 = pow(c, d3, n3).lift()
m1 = pow(m2, d2, n2).lift()
m = pow(m1, d1, n1).lift()
pwn.log.info("decrypted message!")
m_literal = pwn.pack(int(m), 'all', 'big', False)
pwn.log.success("flag: {}".format(m_literal.decode()))

