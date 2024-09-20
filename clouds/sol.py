#!python3
from sage.all import *
from pwn import *

conn = remote("mercury.picoctf.net", 24402)
conn.recvuntil(b"? ")

def store(msg):
    conn.sendline(b"1")
    conn.recvuntil(b": ")
    conn.sendline(msg)
    conn.recvuntil(b"? ")

def retrieve(i):
    conn.sendline(b"2")
    conn.recvuntil(b"? ")
    conn.sendline(str(i).encode())
    msg = conn.recvline().strip()
    conn.recvuntil(b"? ")
    return msg

def sbox(input):
    output = Integer("".join(reversed(input.binary())))
    return output

def sbox_inv(output):
    pass

def mixin_pre(input, key):
    pass

def mixin_pre_inv(output, result):
    pass

def mixin_post(input, key):
    pass

def mixin_post_inv(output, result):
    pass

