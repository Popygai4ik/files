from string import *
slf = '0123456789ABCDEFGHI'
for x in slf:
    s = int(f"55{x}36", 19) + int(f"{x}2524", 19)
    if s %11==0:
        print(x, s // 11)