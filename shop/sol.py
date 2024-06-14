#!/home/maxime/.pyvenv/bin/python3

with open("flag", 'r') as f:
    flag_list = f.read()
    flag_tmp = flag_list.replace('[', '').replace(']', '').strip().split(' ')
    print(''.join(map(lambda a: chr(int(a)), flag_tmp)))

