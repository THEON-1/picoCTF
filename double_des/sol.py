#!python3
from pwn import *
from Crypto.Cipher import DES

#conn = process(["python3", "./ddes.py"])
conn = remote("mercury.picoctf.net", 5958)
conn.recvline()
flag_encrypted = unhex(conn.recvline())
log.info("encrypted flag: {}".format(enhex(flag_encrypted)))
conn.recvuntil(b"? ")

def encrypt_remote(data):
    conn.sendline(enhex(data).encode())
    enc = unhex(conn.recvline())
    conn.recvuntil(b"? ")
    return enc

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + b" " * pad)

def des(data1, data2, k):
    cipher = DES.new(k, DES.MODE_ECB)
    return (cipher.encrypt(data1), cipher.decrypt(data2))

def ddes(data, k1, k2):
    cipher1 = DES.new(k1, DES.MODE_ECB)
    cipher2 = DES.new(k2, DES.MODE_ECB)
    return cipher1.decrypt(cipher2.decrypt(data))

msg = b"abcdef"
log.info("encrypting message remotely: {}".format(msg.decode()))
denc = encrypt_remote(msg)
log.info("encrypted message: {}".format(enhex(denc)))
conn.close()

a, b = des(pad(msg), pad(msg), b"123456  ")
c, d = des(b, a, b"123456  ")
assert c == d

to_enc = pad(msg)
to_dec = denc
P = log.progress("calculating encryptions...")
keyspace = 10**6
encs = set()
encs_dict = {}
decs = set()
decs_dict = {}
for i in range(keyspace):
    k = pad(str(i).encode())
    a, b = des(to_enc, to_dec, k)
    a = enhex(a)
    b = enhex(b)
    encs.add(a)
    encs_dict[a] = i
    decs.add(b)
    decs_dict[b] = i

collisions = encs & decs
P.success("{} collision(s) found".format(len(collisions)))
collision = collisions.pop()
k1 = pad(str(encs_dict[collision]).encode())
k2 = pad(str(decs_dict[collision]).encode())
log.info("k1: {}".format(k1.decode()))
log.indented("k2: {}".format(k2.decode()))

flag = ddes(flag_encrypted, k1, k2)
log.success("flag: {}".format(flag.decode()))

