#!/home/maxime/.pyvenv/bin/python3
from base64 import b64decode
from urllib.parse import unquote

S = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm" + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2" + "JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2"
S = b64decode(S)
S = unquote(S)
print(S)

