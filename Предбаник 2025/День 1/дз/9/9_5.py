f = open('9.2.xlsx - Лист1.csv')
c = 0
for s in f:
    a = list(map(int, s.split(',')))
    if True:
        c += 1
print(c)