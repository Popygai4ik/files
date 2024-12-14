from string import *
slf = '0123456789ABCDEFGH'
for x in slf:
    s = int(f"AB5{x}3", 18) + int(f"EF{x}13", 18)
    if s %17==0:
        print(x, s // 17)