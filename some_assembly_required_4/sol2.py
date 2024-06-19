#!/home/maxime/.pyvenv/bin/python3
from wasmtime import Store, Module, Instance
import string
import itertools

store = Store()
module = Module.from_file(store.engine, "assembly4.wat")
instance = Instance(store, module, [])

exports = instance.exports(store)
memory = exports["memory"]
check_flag = exports["check_flag"]

def init_flag(pair):
    for i in range(len(flag)):
        memory.data_ptr(store)[1072+i]=ord(flag[i])
    for j in range(len(flag_so_far)):
        memory.data_ptr(store)[1072+8+j]=ord(flag_so_far[j])
    memory.data_ptr(store)[1072+8+len(flag_so_far)]=ord(pair[0])
    memory.data_ptr(store)[1072+8+len(flag_so_far)+1]=ord(pair[1])

def count_match():
    count = 0
    while memory.data_ptr(store)[1024+count] == memory.data_ptr(store)[1072+count]:
        count += 1
    return count

flag = "picoCTF{0123456789abcdef123456789abcdef}"
flag_chars = string.ascii_lowercase + string.digits + "_}\x00 "
flag_so_far = ""
for i in range(24):
    for j in itertools.product(flag_chars, repeat=2):
        init_flag(j)
        check_flag(store)
        if count_match() >= 10 + len(flag_so_far):
            flag_so_far += (j[0]+j[1])
            print("picoCTF{" + flag_so_far)
            break

