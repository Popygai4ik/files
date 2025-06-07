f = open('9-7.csv')
c = 0
for s in f:
    a = list(map(int, s.split(',')))
    pov = [x for x in a if a.count(x) > 1]
    ne_pov = [x for x in a if a.count(x) == 1]
    if len(pov) == 2 and len(ne_pov) == 2 and all((d % 2 == 0) for d in ne_pov) and all((d % 2 != 0) for d in pov):
        c +=1
print(c)
