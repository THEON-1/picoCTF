#!python3
from pwn import *
from itertools import chain, combinations

choice = 6
length = 7

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

log.info("reading file")
with open("output.txt", 'r') as f:
    c = int(f.read().strip(), 16)
log.info("read in cyphertext: {:x}".format(c))

c = pack(c, 'all', 'big', False)

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

def decrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

log.info("generating key candidates...")
i = 0
candidates = []
for ss in powerset(random_strs):
    _c = c
    for s in ss:
        _c = decrypt(_c, s)
    _c = decrypt(_c, b'picoCTF{')
    _c = _c.decode()
    if _c[0:8].isprintable():
        log.indented("{:2}: {}".format(i, _c[0:8]))
        candidates.append((_c[0:8], ss))
        i += 1

key = candidates[choice][0][0:length].encode()
decrypt_set = candidates[choice][1]
log.success(key.decode())
for word in decrypt_set:
    c = decrypt(c, word)
c = decrypt(c, key)
log.success("flag found: {}".format(c))

