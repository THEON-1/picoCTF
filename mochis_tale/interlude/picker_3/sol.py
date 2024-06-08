#!/home/maxime/.pyvenv/bin/python3

with open("hex", 'r') as f:
    print(''.join(map(lambda a: chr(int(a, 16)), f.readline().strip().split(' '))))

