#!/home/maxime/.pyvenv/bin/python3

for c in range(5, 0, -1):
 with open("Item0" + str(c) + "_cp.bmp", 'rb') as f:
    img = f.read()

    leading_space = 2019
    flag_size = 10
    enc_size = flag_size * (8 + 4)

    enc_buffer = img[leading_space:leading_space + enc_size]
    flag_buffer = [''] * flag_size

    for i in range(flag_size):
        char = 0
        enc_offset = i * (8 + 4)

        for j in range(8):
            char |= (enc_buffer[enc_offset+j] & 1) << j

            flag_buffer[i] = chr(char)

    print(''.join(flag_buffer), end='')

print()

