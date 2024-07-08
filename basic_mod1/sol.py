#!/home/maxime/.pyvenv/bin/python3

with open("message.txt", 'r') as f:
    text = f.read().strip()

    cipher = text.split(' ')

    dec = ""
    for i in cipher:
        i = int(i)
        i %= 37
        if i <= 25:
            dec += chr(ord('a') + i)
        elif i <= 35:
            dec += chr(ord('0') + i - 26)
        elif i == 36:
            dec += '_'
    print(dec)

