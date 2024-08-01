#!python3
from pwn import *
import re

def pollard_rho(n):
    x0 = 2
    d = 1
    while True:
        if x0 == n:
            return -1
        x = x0
        y = x
        g = lambda x: (pow(x, 2, n) + 1)%n
        while d == 1:
            x = g(x)
            y = g(g(y))
            d = math.gcd(abs(x-y), n)
        if d == n:
            x0 += 1
        else:
            return d

with open("cert.plaintext", 'r') as f:
    lines = f.readlines()

modulus = lines[13].strip()
modulus = int(re.findall("\(.*\)", modulus)[0][3:-1], 16)
log.info("modulus: {}".format(modulus))

exponent = lines[14].strip()
exponent = int(re.findall("\(.*\)", exponent)[0][3:-1], 16)
log.info("exponent: {}".format(exponent))

signature = lines[17:-13]
signature = int(''.join(map(lambda l: l.strip(), signature)).replace(':', ''), 16)
log.info("signature:")
log.hexdump(pack(signature, 'all', 'big', False))

log.info("factoring modulus")
p = pollard_rho(modulus)
q = modulus//p
assert p*q == modulus
log.success("p: {}".format(p))
log.success("q: {}".format(q))

log.success("flag1: picoCTF{{{},{}}}".format(p, q))
log.success("flag2: picoCTF{{{},{}}}".format(q, p))

