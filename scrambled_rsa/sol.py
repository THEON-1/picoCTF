#!python3
from pwn import *
from sage.all import Integer
from string import ascii_lowercase, ascii_uppercase, digits

conn = remote("mercury.picoctf.net", 4484)

conn.recvuntil(b": ")
flag = conn.recvline().strip()
conn.recvuntil(b"n: ")
n = Integer(conn.recvline())
conn.recvuntil(b"e: ")
e = Integer(conn.recvline())

def remote_encrypt(msg):
    conn.recvuntil(b"me: ")
    conn.sendline(msg)
    conn.recvuntil(b"go: ")
    return conn.recvline().strip()

#'''
charset = ascii_lowercase + digits + "_" + ascii_uppercase + "{}"
C_residue = flag
msg = b""
known_encs = []
P = log.progress("bruteforcing message")
while len(C_residue) > 0:
    P.status(msg.decode())
    for new_char in charset:
        new_char = new_char.encode()
        new_msg = msg + new_char
        new_enc = remote_encrypt(new_msg)
        for enc in known_encs:
            new_enc = new_enc.replace(enc, b"")
        if new_enc in C_residue:
            msg += new_char
            known_encs.append(new_enc)
            C_residue = C_residue.replace(new_enc, b"")
            break
P.success(msg.decode())
log.info("message: {}".format(msg))
#'''

