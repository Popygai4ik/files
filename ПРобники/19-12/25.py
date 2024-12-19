from fnmatch import *

for i in range(0, 100000000, 151):
    if fnmatch(str(i), '10?4??9'):
        if i % 151 == 0:
            print(i)