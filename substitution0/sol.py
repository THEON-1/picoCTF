#!/home/maxime/.pyvenv/bin/python3

key = "OHNFUMWSVZLXEGCPTAJDYIRKQB"

D = {}
for i, char in enumerate(key):
    D[char] = chr(ord('A') + i)
    D[char.lower()] = chr(ord('a') + i)

with open("message.txt", 'r') as f:
    for char in f.read():
        if char in D:
            print(D[char], end='')
        else:
            print(char, end='')

print()

