from fnmatch import fnmatch

for i in range(0, 10**9, 222):
    if fnmatch(str(i), '2?269?8*3?'):
        print(i, i / 222)