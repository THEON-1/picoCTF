#!/home/maxime/.pyvenv/bin/python3
from pwn import *
import binascii

def egcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, x1

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def mod_inv(x, modulus):
    g, x, _ = egcd(x, modulus)
    if g != 1:
        raise Exception("gcd(d, lambda_n != !")
    return x % modulus 

# -------------------------------------------------------------------

conn = remote("mercury.picoctf.net", 60368)
conn.recvuntil(b':')
n = conn.recvline().strip()
conn.recvuntil(b':')
e = conn.recvline().strip()
conn.recvuntil(b':')
c = conn.recvline().strip()
conn.recvuntil(b':')

n = int(n)
e = int(e)
c = int(c)

print("n:", n)
print("e:", e)
print("c:", c)

r = 11
r_inv = mod_inv(r, n)
c_ = (c*pow(r, e, n))%n

conn.sendline(str(c_).encode('utf-8'))
conn.recvuntil(b':')
c_dec = conn.recvline().strip()
c_dec = int(c_dec)

flag = (c_dec*r_inv)%n

flag = binascii.unhexlify('{:x}'.format(flag))

print(flag)

