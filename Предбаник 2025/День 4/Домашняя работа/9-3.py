f = open('9_3.csv')
c= 0
for s in f:
    a = list(map(int, s.split(',')))
    if len(set(a)) == 5 and (3 * (min(a) + max(a)) >= 2* (sum(a) - min(a) - max(a))):
        c+= 1
print(c)