#!/home/maxime/.pyvenv/bin/python3

with open("message.txt", 'r') as f:
    text = f.read().strip()
    decoded = ""
    for i in range(len(text)):
        k = i // 3
        j = (i-1)%3
        decoded += text[3*k+j]
    print(decoded)

