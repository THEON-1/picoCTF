#!/home/maxime/.pyvenv/bin/python3

def int2chr(a):
    a = a.strip()
    if a in "{}":
        return a
    else:
        return chr(int(a) + ord('a') - 1)

with open("numbers", 'r') as f:
    digits = f.read().split(' ')
    print(''.join(map(int2chr, digits)))

