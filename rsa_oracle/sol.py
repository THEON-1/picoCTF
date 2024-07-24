#!/home/maxime/.pyvenv/bin/python3
from pwn import *

conn = remote("titan.picoctf.net", 61532)

conn.recvuntil(b"decrypt. \n")
conn.sendline(b"e")
conn.recvuntil(b"size): ")
conn.sendline(b"\x02")

conn.recvuntil(b"Hex m: ")
encoded_modifier = conn.recvline()

if not int(encoded_modifier, 16) == 2:
    log.error("modifier does not match encoded modifier!")

conn.recvuntil(b"mod n) ")
encrypted_modifier = int(conn.recvline())

with open("password.enc") as f:
    password_enc = int(f.read())

conn.recvuntil(b"decrypt. \n")
conn.sendline(b"d")
conn.recvuntil(b"decrypt: ")
conn.sendline(str(password_enc * encrypted_modifier).encode())
conn.recvuntil(b"mod n): ")
password_modified_hex = int(conn.recvline(), 16)
conn.recvuntil(b"text: ")
password_modified = conn.recvline()

if not password_modified == pack(password_modified_hex, 'all', 'big', False):
    log.error("received modified password does not match hex!")

password = password_modified_hex // 2
if not password_modified_hex % 2 == 0:
    log.error("modifier does not divide modified password!")
password = pack(password, 'all', 'big', False)
log.success("found password: {}".format(password))

