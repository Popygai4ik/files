from re import *

for i in range(0, 10**7, 403):
    if fullmatch('12\d*\d1\d*5', str(i)):
        print(i, i // 403)
