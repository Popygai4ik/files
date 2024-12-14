from fnmatch import fnmatch
from re import *

for i in range(0, 10**8, 343):
    # if fullmatch('37\d*87\d', str(i)):
        # print(i, i // 2023, 'R')
    if fnmatch(str(i), '51?32*8'):
        print(i, i // 343, 'M')