#!/home/maxime/.pyvenv/bin/python3

with open("mystery.png", 'rb') as f1, open("mystery2.png", 'rb') as f2, open("mystery3.png", 'rb') as f3:
    img1 = f1.read()
    img2 = f2.read()
    img3 = f3.read()

    contents1 = img1[-16:]
    contents2 = img2[-2:]
    contents3 = img3[-8:]

    flag = ['']*26

    flag[0] = chr(contents2[0] - 21)
    flag[1] = chr(contents3[0])
    flag[2] = chr(contents3[1])
    flag_3_offset = 0
    flag[4] = chr(contents1[0])
    flag[5] = chr(contents3[2])

    for i in range(6, 10):
        flag_3_offset -= 1
        flag[i] = chr(contents1[1+i-6])
    
    flag[3] = chr(contents2[1] + flag_3_offset)

    for i in range(10, 15):
        flag[i] = chr(contents3[3+i-10])

    for i in range(15, 26):
        flag[i] = chr(contents1[5+i-15])

    print(''.join(flag))

