#!/home/maxime/.pyvenv/bin/python3

with open("table.txt", 'r') as f, open("key", 'r') as g, open("enc_flag", 'r') as h:
    lines = f.readlines()
    key = g.read().strip()
    enc_flag = h.read().strip()
    flag = "picoCTF{"
    assert len(enc_flag) == len(key)
    for p, q in zip(enc_flag, key):
        flag += chr((ord(p) - ord(q)) % 26 + ord('A'))
    flag += '}'
    print(flag)

