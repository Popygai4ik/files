# 123*578
i = 12345678
print(str(i)[:3])
print(str(i)[-3:])
for i in range(31, 10**8, 31):
    if str(i)[:3] == '123' and str(i)[-3:] == '578' and i % 31 == 0:
        print(i, i / 31)