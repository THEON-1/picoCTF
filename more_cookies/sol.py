#!/home/maxime/.pyvenv/bin/python3
from base64 import b64decode, b64encode
import requests
from tqdm import tqdm

address = "http://mercury.picoctf.net:34962/"

r = requests.Session()
r.get(address)
s = r.cookies["auth_name"]
s = b64decode(s)
s = b64decode(s)

for i in tqdm(range(len(s))):
    for j in range(8):
        a = s[:i]
        b = s[i+1:]
        l = a + ((s[i] ^ (1 << j)).to_bytes(1, "big")) + b
        cookie = {'auth_name': b64encode(b64encode(l)).decode()}
        r = requests.get(address, cookies=cookie)
        if "picoCTF{" in r.text:
            print(r.text)
            exit()

