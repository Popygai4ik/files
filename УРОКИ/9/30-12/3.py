f = open('3.txt')
c = 0
for s in f:
    data = list(map(int, s.split()))
    pov = [x for x in data if data.count(x) > 1]
    ne_pov = [x for x in data if data.count(x)  == 1]
    if len(pov) == 0 or len(ne_pov) == 0:
        continue
    sr = sum(pov)/len(pov)
    if len(pov) == 3 and len(ne_pov)  == 4 and sr > max(ne_pov):
        c +=1
print(c)
