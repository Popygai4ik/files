from string import *
slf = '0123456789ABCDEFGHIJ'
for x in slf:
    s = int(f"13{x}CF", 20) + int(f"47GH{x}", 20)
    if s %19==0:
        print(x, s // 19)