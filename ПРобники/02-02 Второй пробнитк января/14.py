import string
alf = '0123456789ABCDEFGHIJKLM'
# print(int(alf, 23))
for x in alf:
    for y in alf:
        if (int('13'+y+x+'9', 23) +int('22'+y+'22', 23)) % 2 != 0:
            break
    else:
        print(x, (int('13'+'6'+x+'9', 23) +int('22'+'6'+'22', 23)) // 18)