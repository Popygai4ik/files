f = open('9.6.xlsx - Лист1.csv')
c = 0
for s in f:
    a = list(map(int,s.split(',')))
    pov = [x for x in a if a.count(x) > 1]
    ne_pov = [x for x in a if a.count(x) == 1]
    if sum(ne_pov) % 2 != 0 and len(pov) > 0:
        c += 1
print(c)