#!/home/maxime/.pyvenv/bin/python3

with open("string", 'r') as f:
    line = f.readline().strip()
    chars = line.split(' ')
    chars = map(lambda a: chr(int(a, 16)), chars)
    print(''.join(chars))

