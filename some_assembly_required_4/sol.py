#!/home/maxime/.pyvenv/bin/python3
import string

mem_str = b"\x18j|a\x118i7[H~Jh^Ko\x1f]\x5cw4kP\x15pO?\x5cEo\x14\x06\x05}>=\x04\x16.\x12L\x00\x00"
reference = b"picoCTF{"

corr_mem_str = b""
for i in range(0, len(mem_str)-1, 2):
    corr_mem_str += chr(mem_str[i+1]).encode() + chr(mem_str[i]).encode()

def shift_fwrd(char):
    if char // 128 > 0:
        return char | 0xffffff00
    else:
        return char

def shift_bwrd(char):
    char &= 0xff
    return char

def transform(S,enc):
    result = b""
    temp = ""
    if enc == 0:
        for i in range(0, len(S)-1, 2):
            temp += chr(S[i+1]) + chr(S[i])
        S = temp.encode()
    for i in range(len(S)):
        if enc > 0:
            buf = result
            shift_fun = shift_fwrd
        else:
            buf = S
            shift_fun = shift_bwrd
        char = S[i]
        char = shift_fwrd(char)
        char ^= 20
        if i > 0:
            prev = buf[i-1]
            #prev = shift_fun(prev)
            #char = shift_fun(char)
            char ^= prev
        if i > 2:
            prev = buf[i-3]
            #prev = shift_fun(prev)
            #char = shift_fun(char)
            char ^= prev
        m10 = i%10
        #char = shift_fun(char)
        char ^= m10
        if i%2 == 0:
            #char = shift_fun(char)
            char ^= 9
        else:
            #char = shift_fun(char)
            char ^= 8
        if i%3 == 0:
            #char = shift_fun(char)
            char ^= 7
        elif i%3 == 1:
            #char = shift_fun(char)
            char ^= 6
        else:
            #char = shift_fun(char)
            char ^= 5

        result += chr(char).encode()
    return result

print(transform(mem_str, 0))

temp = ""
next_found = False
for i in range(0, len(mem_str)-1, 2):
    temp += chr(mem_str[i+1]) + chr(mem_str[i])
mem_str = temp.encode()
print(mem_str)

temp = ""
while True:
    for char in string.punctuation+string.ascii_letters + string.digits+' ':
        result = transform((temp+char).encode(), 1)
        if result in mem_str[:len(temp)+1]:
            temp += char
            next_found = True
            break
    if next_found:
        next_found = False
    else:
        print(temp)
        break

