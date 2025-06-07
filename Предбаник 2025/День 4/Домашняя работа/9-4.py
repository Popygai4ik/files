f = open('9-4.csv')
c = 0
for s in f:
    a = list(map(int, s.split(',')))
    pov = [x for x in a if a.count(x) > 1]
    ne_pov = [x for x in a if a.count(x) == 1]
    if len(pov) == 4 and len(ne_pov) == 3 and (sum(ne_pov)/len(ne_pov)) > max(pov):
        c+=1
print(c)