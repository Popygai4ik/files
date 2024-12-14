from fnmatch import fnmatch

for n in range(0, int('FFFFFF', 16), 123):
    if fnmatch(hex(n)[2:], 'f5*1?4'):
        print(hex(n)[2:], n //123)