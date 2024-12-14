from fnmatch import fnmatch
from re import *

for n in range(0, 10**10+1, 5943):
    # if fullmatch('73\d*\d859\d', str(n)):
    #     print(n, n //5943)
    if fnmatch(str(n), '73*?859?'):
        print(n, n //5943)
