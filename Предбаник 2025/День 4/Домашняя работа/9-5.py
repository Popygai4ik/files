f = open('9.5.xlsx - Лист1.csv')
c = 0
for s in f:
    a = list(map(int,s.split(',')))
    pov = [x for x in a if a.count(x) > 1]
    ne_pov = [x for x in a if a.count(x) == 1]
    if len(set(a)) == 4 and (sum(pov) < sum(ne_pov)):
        c += 1
print(c)