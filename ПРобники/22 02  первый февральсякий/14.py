alf = '0123456789ABCDEF'
# import string
for i in alf:
    s1 = int(f'{i}432',16)

    s2 = int(f'234{i}',16)
    if (s1 + s2)% 15 == 0:
        print(s1, s2, i)