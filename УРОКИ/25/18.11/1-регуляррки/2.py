from re import *

for i in range(0, 10**9, 127):
    if fullmatch('215\d*414\d', str(i)):
        print(i, i // 127)