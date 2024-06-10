#!/home/maxime/.pyvenv/bin/python3

with open("encoded.bmp", 'rb') as f:
    img = f.read()
    flag_len = 50
    stego_len = flag_len * 8
    stego_start = 2000
    encoded_bytes = img[stego_start:stego_start + stego_len]

    flag_buffer = [''] * flag_len
    for i, flag_char in enumerate(flag_buffer):
        char = 0
        for j in range(8):
            img_char = encoded_bytes[i*8+j]
            char |= (img_char & 1) << j
        flag_buffer[i] = chr(char + 5)

print(''.join(flag_buffer))

