f = open('2.txt')
c = 0
for s in f:
    a = list(map(int, s.split()))
    # print(a)
    pov = [x for x in a if a.count(x) > 1]
    print(set(a))
    ne_pov = [x for x in a if a.count(x) == 1]
    print(ne_pov)
    if len(ne_pov) == 4 and sum(pov) < sum(ne_pov):
        c += 1
    if len(set(a)) == 4 and sum(pov) < sum(ne_pov):
        c += 1
print(c)

