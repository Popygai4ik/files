f = open('9.2_8xrKMYb.csv')
c = 0
for s in f:
    a = list(map(int, s.split(',')))
    pov = [i for i in a if a.count(i) > 1]
    ne_pov = [i for i in a if a.count(i) == 1]
    if len(pov) == 4 and len(ne_pov) == 4 and (min(a) in pov):
        c+= 1
print(c)x