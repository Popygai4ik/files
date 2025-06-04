f = open('9_0JcUYgk.csv')
c = 0
for s in f:
    a = list(map(int, s.split(',')))
    chet = [i for i in a if i % 2 == 0]

    # ne_pov = [i for i in a if a.count(i) == 1]
    if len(chet) == 4 and (min(a)**2 <= (sum(a) - min(a))):
        c+= 1
print(c)