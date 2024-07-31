#!python3
from sage.all import *
import pwn

e = 3
pairs = []
pwn.log.info("reading file")
with open("encrypted-messages.txt", 'r') as f:
    lines = f.readlines()

    for i in range(12):
        j = 4*i
        N = Integer(lines[j][3:].strip())
        e = Integer(lines[j+1][3:].strip())
        c = Integer(lines[j+2][3:].strip())
        pairs.append((N, c))

# filter other messages
pwn.log.info("filtering non-flag messages")
msgs = [
    b'I just cannot wait for rowing practice today!',
    b'I hope we win that big rowing match next week!',
    b'Rowing is such a fun sport!'
        ]
flag_pairs = []
for N, c in pairs:
    is_flag = True
    for msg in msgs:
        m = pwn.unpack(msg, 'all', endian='big', sign=False)
        if pow(m, e, N) == c:
            is_flag = False
    if is_flag:
        flag_pairs.append((N, c))

pwn.log.debug("found {} flag pairs".format(len(flag_pairs)))

# chinese remainder theorem
pwn.log.info("computing m")
a = []
b = []
for N, c in flag_pairs:
    a.append(c)
    b.append(N)
m_e = crt(a, b)
pwn.log.info("found m^e")
pwn.log.debug("m_e: {}".format(m_e))
pwn.log.info("calculating m")
m = m_e.nth_root(e)
pwn.log.debug("m: {}".format(m))
m_literal = pwn.pack(int(m), 'all', 'big', False)
pwn.log.success("found flag: {}".format(m_literal.decode()))

