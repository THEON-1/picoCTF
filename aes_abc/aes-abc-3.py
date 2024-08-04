#!python3

from Crypto.Cipher import AES
import os
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
        

def pad(pt):
    padding = BLOCK_SIZE - len(pt) % BLOCK_SIZE
    return pt + (bytes([padding]) * padding)


def aes_abc_encrypt(pt):
    KEY = b"0123456789abcdef"
    cipher = AES.new(KEY, AES.MODE_ECB)
    ct = cipher.encrypt(pad(pt))

    blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) // BLOCK_SIZE)]
    iv = b"0123456789abcdef"
    blocks.insert(0, iv)
    
    for i in range(len(blocks) - 1):
        prev_blk = int(blocks[i].hex(), 16)
        curr_blk = int(blocks[i+1].hex(), 16)

        n_curr_blk = (prev_blk + curr_blk) % UMAX
        blocks[i+1] = n_curr_blk.to_bytes(BLOCK_SIZE, 'big')

    ct_abc = b"".join(blocks)

    _blocks = [ct_abc[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct_abc) // BLOCK_SIZE)]
    assert len(blocks) == len(_blocks)
    assert blocks == _blocks
    for i in reversed(range(len(_blocks)-1)):
        prev_blk = int.from_bytes(_blocks[i], 'big')
        curr_blk = int.from_bytes(_blocks[i+1], 'big')
        n_curr_blk = (curr_blk - prev_blk)%UMAX
        _blocks[i+1] = n_curr_blk.to_bytes(BLOCK_SIZE, 'big')
    _blocks = _blocks[1:]
    assert len(blocks) == len(_blocks)+1
    _ct = b"".join(_blocks)
    assert len(_ct) == len(ct)
    assert _ct == ct
 
    return iv, ct_abc, ct


if __name__=="__main__":
    with open('flag.ppm', 'rb') as f:
        header, data = parse_header_ppm(f)
    
    iv, c_img, ct = aes_abc_encrypt(data)

    with open('test.enc.ppm', 'wb') as fw:
        fw.write(header)
        fw.write(c_img)
