#!/home/maxime/.pyvenv/bin/python3

D = {
    'c': 'p', 'C': 'P',
    'b': 'i', 'B': 'I',
    'z': 'c', 'Z': 'C',
    'j': 'o', 'J': 'O',
    'w': 't', 'W': 'T',
    'd': 'f', 'D': 'F',
    'g': 's', 'G': 'S',
    'v': 'n', 'V': 'N',
    'm': 'd', 'M': 'D',
    'x': 'e', 'X': 'E',
    'f': 'r', 'F': 'R',
    'i': 'm', 'I': 'M',
    'p': 'u', 'P': 'U',
    's': 'y', 'S': 'Y',
    'q': 'l', 'Q': 'L',
    'r': 'g', 'R': 'G',
    'e': 'h', 'E': 'H',
    'h': 'w', 'H': 'W',
    'y': 'v', 'Y': 'V',
    'n': 'k', 'N': 'K',
    't': 'b', 'T': 'B',
    'a': 'a', 'A': 'A',

    'o': 'o', 'O': 'O',
    'u': 'u', 'U': 'U',

    'k': 'k', 'K': 'K',
    'l': 'q', 'L': 'Q',
}

for i in range(26):
    if chr(ord('a') + i) not in D:
        print(chr(ord('a') + i))

print()

with open("message.txt", 'r') as f:
    for char in f.read():
        if char in D:
            print(D[char], end='')
        else:
            print(char, end = '')

print()

