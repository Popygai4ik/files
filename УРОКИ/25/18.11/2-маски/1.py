from fnmatch import fnmatch
c = []
for i in range(0, 100000, 134):
    if fnmatch(str(i), '1?7*'):
        kolvo = str((bin(i)[2:])).count('1')
        c.append(kolvo)
print(*c)