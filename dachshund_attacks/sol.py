#!/home/maxime/.pyvenv/bin/python3
from sympy import Rational, Symbol, solve
from sympy.ntheory.continued_fraction import continued_fraction, continued_fraction_convergents
from pwn import *

conn = connect("mercury.picoctf.net", 30761)
conn.recvuntil(b':')
e = int(conn.recvline().strip())
conn.recvuntil(b':')
n = int(conn.recvline().strip())
conn.recvuntil(b':')
c = int(conn.recvline().strip())
conn.close()

print("n =", n, '\n')
print("e =", e, '\n')
print("c =", c, '\n')


cont_frac = continued_fraction(Rational(e, n))
convergents = continued_fraction_convergents(cont_frac)


for convergent in convergents:
    if convergent.p == 0:
        continue
    pk = convergent.p
    pd = convergent.q
    pphi = (e*pd - 1)//pk

    p = Symbol('p', integer=True)
    roots = solve(p**2 + (pphi - n - 1)*p + n, p)

    if len(roots) == 2:
        pp, pq = roots
        if pp*pq == n:
            print("factorized!")
            P = pow(c, pd, n)
            print(P.to_bytes((P.bit_length()+7)//8, byteorder='big'))
            break


