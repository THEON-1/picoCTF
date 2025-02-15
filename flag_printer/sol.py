#!/usr/bin/env python3
from sage.all import *
MOD = 7514777789

ring=GF(MOD)

points = []
for line in open('encoded.txt', 'r').read().strip().split('\n'):
    x, y = line.split(' ')
    points.append((int(x), int(y)))

print("building matrices")

solution = []
M = []
for point in points:
    x, y = point
    solution.append(ring(y % MOD))

    row = []
    for i in range(3):
        row.append(pow(x, i, MOD))
    M.append(row)

print("converting matrices")

solution = vector(solution)
M = Matrix(M, base_ring=GF(MOD))

print('solving')
open('output.bmp', 'wb').write(bytearray(M.solve_right(solution).tolist()[:-1]))
