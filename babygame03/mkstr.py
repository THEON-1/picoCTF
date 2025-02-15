#!/usr/bin/env python3
from pwn import *

a = 'aaaa'+'a'*4+'wwwws'
b = 'a'*47+'lp'+'ws'

s = a+'p' +a+'p' +a+'p' +a +b +a +'wws\n'

print(s)

