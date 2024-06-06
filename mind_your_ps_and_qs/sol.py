#!/usr/bin/python3
import math

def totient(p, q):
    tot, rem = divmod((p-1) * (q-1), math.gcd(p-1, q-1))
    if rem != 0:
        raise Exception("totient calc failed")
    return tot

def egcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, x1

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def mod_inv(d, lambda_n):
    g, x, _ = egcd(d, lambda_n)
    if g != 1:
        raise Exception("gcd(d, lambda_n != !")
    return x % lambda_n

def rsa(text, key, n):
    return pow(text, key, n)

with open("values", 'r') as f:
    lines = f.readlines()

    C = int(lines[1][3:])
    n = int(lines[2][3:])
    e = int(lines[3][3:])
    p = int(lines[4][3:])
    q = int(lines[5][3:])

    if p*q == n:
        print("factoring correct")
    else:
        print("factoring incorrect")

    lambda_n = totient(p, q)

    d = mod_inv(e, lambda_n)
    #d = pow(d, -1, lambda_n)

    res = rsa(C, d, n)

    text = ''
    while (char := (res % 256)) != 0:
        text = chr(char) + text;
        res >>= 8

    print(text)

