#!python3
import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))

def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index(b'\n') + 1], s[s.index(b'\n')+1:]

def parse_header_ppm(f):
    data = f.read()

    header = b""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data
 
with open("body.enc.ppm", 'rb') as f:
    header, data = parse_header_ppm(f)

blocks = [data[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(data) // BLOCK_SIZE)]

for i in reversed(range(len(blocks) - 1)):
    prev_blk = int.from_bytes(blocks[i], 'big')
    curr_blk = int.from_bytes(blocks[i+1], 'big')

    n_curr_blk = (curr_blk - prev_blk) % UMAX
    blocks[i+1] = n_curr_blk.to_bytes(16, 'big')

blocks = blocks[1:]

with open("body.ppm", 'wb') as f:
    f.write(header)
    for block in blocks:
        f.write(block)

