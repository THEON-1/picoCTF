#!python3
from sage.all import Integer, IntegerRange, GCD
from pwn import *
from Crypto.Hash import MD5

#conn = process(['python3', 'not_my_fault.py'])
conn = remote("mercury.picoctf.net", 48006)
conn.recvuntil(b"\"")
str_start = conn.recvuntil(b"\"")[:-1]
log.info("string start: {}".format(str_start.decode()))
conn.recvuntil(b": ")
hash_end = conn.recvline().strip().decode()
log.info("hash end: {}".format(hash_end))

P = log.progress("bruteforcing hash")
hash = "0"*32
i = 0
while hash[-6:] != hash_end:
    md5 = MD5.new()
    str_to_hash = str_start + str(i).encode()
    md5.update(str_to_hash)
    hash = md5.hexdigest()
    if i%100000 == 0:
        P.status("msg: {} {}| hash end: {}".format(str_start.decode(), str(i).ljust(12), hash[-6:]))
    i += 1
P.success("msg: {} {}| hash end: {}".format(str_start.decode(), str(i).ljust(16), hash[-6:]))
conn.sendline(str_to_hash)

conn.recvuntil(b" : ")
n = Integer(conn.recvline())
log.info("modulus: {}".format(hex(n)))

conn.recvuntil(b" : ")
ce = Integer(conn.recvline())
log.info("clue: {}".format(hex(ce)))

P = log.progress("bruteforcing p by guessing d_p: ")
n_bits = 20
limit = 1 << n_bits
m = Integer(3)
for _d_p in IntegerRange(1, limit):
    if _d_p%2000 == 0:
        P.status("{} ({:.1%})".format(_d_p, float(_d_p/limit)))
    gcd = GCD(m-pow(m, ce*_d_p, n), n)
    if gcd != 1 and gcd != n:
        p = gcd.lift()
P.success("{} ({:.1%})".format(_d_p, float(_d_p/limit)))
assert n%p == 0
log.success("found p: {}".format(p))

q = n//p
assert p*q == n
conn.sendline(str(p+q).encode())
flag = conn.recvline()
log.success("flag: {}".format(flag.decode()))


