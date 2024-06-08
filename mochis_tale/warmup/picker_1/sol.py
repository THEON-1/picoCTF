#!/home/maxime/.pyvenv/bin/python3

with open("code", 'r') as f:
    line = f.readline()
    print(''.join(map(lambda a: chr(int(a, 16)), line.strip().split(' '))))

