f = open('9.2.xlsx - Лист1.csv')
c= 0
for s in f:
    a = list(map(int,s.split(',')))
    pov = [x for x in a if a.count(x) > 1]
    ne_pov = [x for x in a if a.count(x) == 1]
    if len(pov) > 0 and ((sum(ne_pov)/len(ne_pov) ) >= (sum(pov)/len(pov))):
        c+= 1
print(c)