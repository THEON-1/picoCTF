#!/home/maxime/.pyvenv/bin/python3

with open("encoded.bmp", 'rb') as f:
    img = f.read()
    
    buffer_zone = 732
    flag_size = 50
    enc_size = flag_size * 9

    enc_buffer = img[buffer_zone:buffer_zone + enc_size]
    flag_buffer = [''] * flag_size

    for i in range(flag_size):
        enc_offset = i * 9

        char = 0
        for j in range(8):
            char |= (enc_buffer[enc_offset+j] & 1) << j
        flag_buffer[i] = chr(char)

    print(''.join(flag_buffer))

