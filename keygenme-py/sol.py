#!/home/maxime/.pyvenv/bin/python3
import hashlib

username = b"FRASER"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

user_hash = hashlib.sha256(username).hexdigest()

key = [''] * 8

key[0] = user_hash[4]
key[1] = user_hash[5]
key[2] = user_hash[3]
key[3] = user_hash[6]
key[4] = user_hash[2]
key[5] = user_hash[7]
key[6] = user_hash[1]
key[7] = user_hash[8]

print(key_part_static1_trial + ''.join(key) + key_part_static2_trial)

