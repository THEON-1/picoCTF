#!/home/maxime/.pyvenv/bin/python3
from json import loads
from pwn import *

with open("out.json", 'r') as f:
    text = f.read()
    json = loads(text)
    for frame in json:
        pflag = list(frame["_source"]["layers"]["data-text-lines"].keys())[0].strip()
        pflag_content = pflag[8:-1]
        pflag_content = unhex(pflag_content)
        if pflag_content.isascii():
            print(pflag_content)

