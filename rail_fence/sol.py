#!/home/maxime/.pyvenv/bin/python3

with open("message.txt", 'r') as f:
    text = f.read()

    dec = [" "] * len(text)
    i = 0
    j = 0
    while True:
        dec[j] = text[i]
        i += 1
        j += 6
        if j >= len(text):
            break
    j = 1
    while True:
        dec[j] = text[i]
        i += 1
        j += 4 
        if j >= len(text):
            break
        dec[j] = text[i]
        i += 1
        j += 2
        if j >= len(text):
            break
    j = 2
    while True:
        dec[j] = text[i]
        i += 1
        j += 2
        if j >= len(text):
            break
        dec[j] = text[i]
        i += 1
        j += 4
        if j >= len(text):
            break
    j = 3
    while True:
        dec[j] = text[i]
        i += 1
        j += 6
        if j >= len(text):
            break
    print(''.join(dec))

