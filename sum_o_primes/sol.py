#!python3
from sage.all import *
import pwn

with open("output.txt", 'r') as f:
    lines = f.readlines()
    x = Integer(lines[0][4:], 16)
    N = Integer(lines[1][4:], 16)
    c = Integer(lines[2][4:], 16)

pwn.log.info("x: {}".format(x))
pwn.log.info("N: {}".format(N))
pwn.log.info("c: {}".format(c))

# n = p*q
# x = p+q
# -> n = p*(x-p)
# -> n = px - p²
# -> p² - px + n = 0
# -> (p - x/2)² + n - x²/4 = 0
# -> (p - x/2)² = x²/4 - n
# -> p - x/2 = +- sqrt(x²/4 - n)
# -> p = x/2 +- sqrt(x²/4 - n)

disc = sqrt(pow(x, 2)//4 - N)
p = x//2 + disc
q = x//2 - disc
# since (p, q) can be replaced by (q, p)
assert p+q == x
assert p*q == N
pwn.log.success("calculated p and q")
pwn.log.info("p: {}".format(p))
pwn.log.info("q: {}".format(q))

e = Integer(65537)
d = pow(e, -1, (p-1)*(q-1))
pwn.log.info("calculated d: {}".format(d))

m = pow(c, d, N)
m_literal = pwn.pack(int(m), 'all', 'big', False)
pwn.log.success(m_literal.decode())

