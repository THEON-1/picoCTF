#!/home/maxime/.pyvenv/bin/python3

with open("mystery.png", 'rb') as f:
    image = f.read()
    l = len(image)
    flag_start = l-26

    for i in range(flag_start, l):
        print(chr(image[i]), end='')
    print()

    for i in range(flag_start, flag_start + 6):
        print(chr(image[i]), end='')

    for i in range(flag_start + 6, flag_start + 15):
        print(chr(image[i] - 5), end ='')

    print(chr(image[flag_start + 15] + 3), end='')

    for i in range(flag_start + 16, flag_start + 26):
        print(chr(image[i]), end='')

    print()

