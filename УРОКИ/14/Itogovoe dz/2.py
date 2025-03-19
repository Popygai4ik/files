import string

alf ="0123456789ABCDEF"
for x in alf:
    s1 = int(f'D49{x}1', 16)
    s2 = int(f'48A3{x}', 16)
    if (s2 + s1 ) % 14 == 0:
        print(x, (s2 + s1 ) / 14)