#!/home/maxime/.pyvenv/bin/python3
S = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"

flag = ['']*32

for i in range(31, 16, -2):
    flag[i] = S[i]

for i in range(16, 32, 2):
    flag[46-i] = S[i]

for i in range(8, 16):
    flag[23-i] = S[i]

for i in range(8):
    flag[i] = S[i]

print(''.join(flag))

