from fnmatch import fnmatch

for x in range(0, 10**8, 31):
    if fnmatch(str(x), '123*578'):
        print(x, x // 31)