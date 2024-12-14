from fnmatch import *

for n in range(0, 10**7, 403):
    if fnmatch(str(n), '12*?1*5'):
        print(n, n // 403)