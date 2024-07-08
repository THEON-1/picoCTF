#!/home/maxime/.pyvenv/bin/python3
from math import sqrt

def iroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s

with open("ciphertext", 'r') as f:
    file = f.read().splitlines()
    N = int(file[0][2:].strip())
    e = int(file[1][2:].strip())
    c = int(file[3][16:].strip())

    #sol = 3533
    #'''
    for i in range(10000):
        c_nomod = c+i*N
        p = iroot(e, c_nomod)
        if p**3 == c_nomod:
            print(i)
            break
    #'''
    #p = iroot(e, c+sol*N)

    result = p.to_bytes((p.bit_length()+7)//8, byteorder='big')
    print(result)

