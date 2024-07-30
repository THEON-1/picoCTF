#!python3
from sage.all import *
from sympy.utilities.iterables import multiset_partitions
from pwn import *

port = 62870
conn = remote("saturn.picoctf.net", port)

conn.recvuntil(b"anger = ")
c = Integer(int(conn.recvline()))
log.info("received c: {}".format(c))
conn.recvuntil(b"envy = ")
d = Integer(int(conn.recvline()))
log.info("received d: {}".format(d))
e = Integer(65537)
log.info("preknown e: {}".format(e))

kN = e*d - 1
log.info("kN: {}".format(kN))
kN_factors = factor(kN)
log.info("factorized kN: {}".format(kN_factors))

kN_multiset = []
for a, b in kN_factors:
    for i in range(b):
        kN_multiset.append(a)
log.info("generated multiset: {}".format(kN_multiset))

candidates = []
kN_multiparts = multiset_partitions(kN_multiset, 3)
iLogger = log.progress("checking multiset partitions")
for kN_multipart in kN_multiparts:
    _x = kN_multipart[0]
    _y = kN_multipart[1]
    _z = kN_multipart[2]
    S = [prod(_x), prod(_y), prod(_z)]
    S.sort(reverse=True)
    x, y, z = S
    if y.nbits() == 128:
        if x.nbits() == 128:
            candidates.append((x, y, z))
        elif z.nbits() == 128:
            candidates.append((y, z, x))
iLogger.success("found {} candidates".format(len(candidates)))
solutions = []

for _p, _q, _k in candidates:
    if (_p+1).is_prime() and (_q+1).is_prime():
        p = _p+1
        q = _q+1
        N = p*q
        k = _k
        solutions.append((p, q, N, k))
log.info("found {} solutions".format(len(solutions)))
if len(solutions) != 1:
    log.critical("Too many/little solutions")
    exit(1)

p, q, N, k = solutions[0]
log.success("p: {}".format(p))
log.success("q: {}".format(q))
log.success("N: {}".format(N))
log.success("k: {}".format(k))
m = pow(c, d, N)
log.info("decoded message: {}".format(m))
m_string = pack(int(m), "all", "big", False)
log.info("literal message: {}".format(m_string))

conn.recvuntil(b"> ")
conn.sendline(m_string)

conn.recvuntil(b"Conquered!")
flag = conn.recvuntil(b'}').strip().decode()
log.success("flag: {}".format(flag))

