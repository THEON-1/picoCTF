#!python3
from sage.all import *
from pwn import *

with open("output.txt", 'r') as f:
    lines = f.readlines()
    N = Integer(lines[0][4:].strip(), 16)
    c = Integer(lines[1][4:].strip(), 16)
log.info(f"N: {N}")
log.info(f"c: {c}")

e = Integer(0x10001)
log.info(f"e: {e}")

smooth_bound = 16
loopmsg = log.progress("calculating p, q")
interval = (0, smooth_bound)
center = 0
while True:
    base = Integer(2)
    M = 1
    for p in Primes():
	    if p >= smooth_bound:
	        break
	
	    np = p
	    while np+p < smooth_bound:
	        np += p
	
	    M *= np
    
    g = gcd(pow(base, M, N)-1, N)
    
    if g == 1 and center == 0:
        interval = (smooth_bound, smooth_bound*2)
        smooth_bound *= 2
    elif g == 1 and center != 0:
        interval = (center, interval[1])
        center = interval[0] + (interval[1] - interval[0])/2
        smooth_bound = center
    elif g == N and center == 0:
        center = interval[0] + (interval[1] - interval[0])/2
        smooth_bound = center
    elif g == N and center != 0:
        interval = (interval[0], center)
        center = interval[0] + (interval[1] - interval[0])/2
        smooth_bound = center
    else:
        loopmsg.success("factoring found")
        p = int(g)
        q = N // p
        break

assert p*q == N
log.info(f"p: {p}")
log.info(f"q: {q}")

d = pow(e, -1, (p-1)*(q-1))
log.info(f"d: {d}")

m = pow(c, d, N)
log.info(f"m: {m}")
m_literal = pack(int(m), 'all', 'big', False)
log.success(f"solution: {m_literal}")

