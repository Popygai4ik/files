f = open('2.txt')
c = 0
for s in f:
    data = list(map(int, s.split()))
    pov = [x for x in data if data.count(x) > 1]
    ne_pov = [x for x in data if data.count(x) == 1]
    # print(data, pov, ne_pov)
    if len(pov) == 0 or len(ne_pov) == 0:
        continue
    sr_po = sum(pov)/len(pov)
    sr_ne= sum(ne_pov)/len(ne_pov)
    if len(pov) == 3 and len(ne_pov) == 4 and sr_ne <= sr_po:
        c += 1
print(c)