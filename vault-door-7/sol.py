#!/home/maxime/.pyvenv/bin/python3

I = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734291511, 960049251, 1681089078]

print(''.join(map(lambda a: (chr(a>>24) + chr((a%(2**24))>>16) + chr((a%(2**16))>>8) + chr(a%(2**8))), I)))
