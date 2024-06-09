#!/home/maxime/.pyvenv/bin/python3

row_1 = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98]
row_2 = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
row_3 = [0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o143, 0o61]
row_4 = ['9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e']

print(''.join(
    list(map(lambda a: chr(a), row_1)) +
    list(map(lambda a: chr(a), row_2)) + 
    list(map(lambda a: chr(a), row_3)) +
    row_4
))

