#!/home/maxime/.pyvenv/bin/python3
from base64 import b64decode

with open("flag_enc", 'r') as f:
    text = f.read().replace(' ', '').strip() + '=='
    print(b64decode(text))

