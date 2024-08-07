#!python3
import re
import string

with open("cypher", "r") as f:
    cypher = f.read().strip()
assert len(cypher)%2==0

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
FLAG_ALPHABET = "0123456789abcdef"
FLAG_ALPHABET_B16 = []
a = ord('a')

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def b16_decode(encoded):
    dec = ""
    assert len(encoded)%2 == 0
    for i in range(len(encoded)//2):
        e1 = ALPHABET.index(encoded[2*i])
        e2 = ALPHABET.index(encoded[2*i+1])
        dec += chr((e1<<4) + e2)
    return dec

for c in FLAG_ALPHABET:
    FLAG_ALPHABET_B16.append(b16_encode(c))

KEY_SETS = []
for i in range(len(cypher)//2):
    KEY_SET_0 = set()
    KEY_SET_1 = set()
    char_0 = ALPHABET.index(cypher[i*2])
    char_1 = ALPHABET.index(cypher[i*2+1])
    for flag_char in FLAG_ALPHABET_B16:
        f0 = ord(flag_char[0]) - a
        f1 = ord(flag_char[1]) - a
        k0 = chr((char_0 - f0)%len(ALPHABET)+a)
        k1 = chr((char_1 - f1)%len(ALPHABET)+a)
        KEY_SET_0.add(k0)
        KEY_SET_1.add(k1)
    KEY_SETS.append(KEY_SET_0)
    KEY_SETS.append(KEY_SET_1)

possible_kls = []
for kl in range(2, 16):
    length_doable = True
    key_options = [[]]*kl
    for i in range(kl):
        possible_cs = []
        for c in KEY_SETS[i]:
            c_possible = True
            for j in range(i, len(KEY_SETS), kl):
                if c not in KEY_SETS[j]:
                    c_possible = False
                    break
            if c_possible:
                possible_cs.append(c)
        if len(possible_cs) == 0:
            length_doable = False
            break
        else:
            key_options[i] = possible_cs
    if length_doable:
        possible_kls.append(key_options)
print(len(possible_kls))
key = ""
for kl in possible_kls:
    print(kl)
    for kc in kl:
        key += kc[0]
print(key)

b16_flag = ""
for i, c in enumerate(cypher):
    c = ALPHABET.index(c)
    k = ord(key[i%len(key)])-a
    b16_flag += chr((c - k)%len(ALPHABET)+a)
print(b16_flag)

flag = b16_decode(b16_flag)
print(flag)

