#!/home/maxime/.pyvenv/bin/python3

with open("message.txt", 'r') as f:
    text = f.read().strip()

    cipher = text.split(' ')

    dec = ""
    for i in cipher:
        i = int(i)
        i %= 41
        i = pow(i, -1, 41)
        if i <= 26:
            dec += chr(ord('a') + i - 1)
        elif i <= 36:
            dec += chr(ord('0') + i - 27)
        elif i == 37:
            dec += '_'
    print(dec)

