#!/home/maxime/.pyvenv/bin/python3
from pwn import *

for i in range(0x7e77, 0x10000):
    p = process("./level5.py", shell=True)
    p.recvuntil(b": ")
    p.sendline("{:x}".format(i).encode())
    log.info("trying {:x}".format(i).encode())
    try:
        res = p.recvline_contains(b"picoCTF")
        log.success(res)
        break
    except:
        p.close()

