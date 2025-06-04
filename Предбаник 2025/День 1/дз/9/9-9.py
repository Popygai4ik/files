f = open('9_UuURhCF-9.csv')
c = 0
for s in f:
    a = list(map(int, s.split(',')))
    pov = [i for i in a if a.count(i) > 1]
    ne_pov = [i for i in a if a.count(i) == 1]
    if len(ne_pov) == 5 and (3*(min(a) + max(a))>=(2*(sum(a)-(min(a) + max(a))))):
        c+= 1
print(c)