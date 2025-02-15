#!/usr/bin/env python3
import galois
import numpy as np
MOD = 7514777789

points = []

for line in open('encoded.txt', 'r').read().strip().split('\n'):
    x, y = line.split(' ')
    points.append((int(x), int(y)))

GF = galois.GF(MOD)
print(GF.properties)

matrix = []
solution = []
for point in points:
    x, y = point
    solution.append(GF(y % MOD))

    row = []
    for i in range(3):
        row.append(GF((x ** i) % MOD))
    
    matrix.append(GF(row))

print('solving')
open('output.bmp', 'wb').write(bytearray(np.linalg.lstsq(GF(matrix), GF(solution)).tolist()[:-1]))
