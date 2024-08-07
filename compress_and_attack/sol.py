#!python3
from pwn import *
import string
import ast

#conn = process(["python3", "compress_and_attack.py"])
conn = remote("mercury.picoctf.net", 2431)
conn.recvuntil(b": ")

def encrypt(text):
    conn.sendline(text)
    nonce = ast.literal_eval(conn.recvline().decode())
    encrypted = ast.literal_eval(conn.recvline().decode())
    length = int(conn.recvline())
    conn.recvuntil(b": ")
    
    return nonce, encrypted, length

CHARACTERSET = string.ascii_lowercase + string.digits + " }_"

prefix = "picoCTF{"
pre_known = "sheriff_you_solved_"

max_chars = 20
sol_char = prefix[-1]
sol_string = prefix+pre_known
while sol_char != '}':
    P = log.progress("trying characters... ")
    min_char = ""
    min_size = 1000000000000000000000000000000000
    for c in CHARACTERSET:
        P.status(sol_string+c)
        s = 0
        n = 1
        for _ in range(n):
            _, encrypted, _ = encrypt((sol_string+c).encode())
            s += len(encrypted)
        if s < min_size:
            min_char = c
            min_size = s
    
    sol_char = min_char
    sol_string += min_char
    P.success(sol_string)
    
