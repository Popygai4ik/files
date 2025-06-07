c = 0
f=open('9 Лист1.csv')
for s in f:
    a = list(map(int,s.split(',')))
    pov = [x for x in a if a.count(x) > 1]
    ne_pov = [x for x in a if a.count(x) == 1]
    if len(pov) == 3 and len(ne_pov) == 4 and ((sum(ne_pov)/len(ne_pov)) <=(sum(pov)/len(pov))):
        c += 1
print(c)