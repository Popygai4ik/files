from fnmatch import *
for n in range(1,10**9):
    if fnmatch(str(n),'7*2??6?*') and n % 16 == 0 and n % 9 != 0:
        print(n)

