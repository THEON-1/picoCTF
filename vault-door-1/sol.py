#!/home/maxime/.pyvenv/bin/python3

S = '''
               password.charAt(0)  == 'd' &&
               password.charAt(1)  == '3' &&
               password.charAt(2)  == '5' &&
               password.charAt(3)  == 'c' &&
               password.charAt(4)  == 'r' &&
               password.charAt(5)  == '4' &&
               password.charAt(7)  == 'b' &&
               password.charAt(17) == '4' &&
               password.charAt(23) == 'r' &&
               password.charAt(29) == '3' &&
               password.charAt(10) == '_' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == 'f' &&
               password.charAt(30) == 'b' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '6' &&
               password.charAt(26) == 'f' &&
               password.charAt(31) == '0'
 '''

l = list(map(lambda a: [int(a[0]), a[1]], map(lambda a: a.strip().replace("  ", ' ').split(' '), S.strip().replace("password.charAt(", '').replace(')', '').replace(" &&", '').replace("== ", '').splitlines())))
l.sort()
print(''.join(map(lambda a: a[1].replace('\'', ''), l)))

