#!/home/maxime/.pyvenv/bin/python3

def switch(i, a, b):
    #print(bin(i))

    mask_a = 1<<a
    mask_b = 1<<b
    #print(bin(mask_a), bin(mask_b))

    bit_a = i & mask_a
    bit_b = i & mask_b
    #print(bin(bit_a), bin(bit_b))

    rest = i & ((mask_a | mask_b) ^ 0xff)
    #print(bin(rest))

    if bit_a:
        rest |= mask_b
    if bit_b:
        rest |= mask_a
    #print(bin(rest))
    #print()

    return rest

hex = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86,
       0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC2, 0xD2, 0x95, 0xA4, 0xF0, 0xD2, 0xD2, 0xC1, 0x95]

for c in hex:
    c = switch(c, 6, 7)
    c = switch(c, 2, 5)
    c = switch(c, 3, 4)
    c = switch(c, 0, 1)
    c = switch(c, 4, 7)
    c = switch(c, 5, 6)
    c = switch(c, 0, 3)
    c = switch(c, 1, 2)
    print(chr(c), end='')

print()

