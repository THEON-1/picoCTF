#!/home/maxime/.pyvenv/bin/python3
from pwn import *

s = ssh(host="mimas.picoctf.net", user="ctf-player" , port=50061, password="6abf4a82")
#sh = s.shell(tty=True)

