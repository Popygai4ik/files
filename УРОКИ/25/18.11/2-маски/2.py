from fnmatch import fnmatch

for x in range(0, 10**8, 98):
    if fnmatch(str(x), '12*678?'):
        print(x, x // 98)