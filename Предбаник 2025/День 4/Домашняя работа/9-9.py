f= open('9_9.csv')
c = 0
for n,e in enumerate(f,1):
    a = list(map(int,e.split(',')))
    ne_pov = [x for x in a if a.count(x) == 1]
    krat = [x for x in a if x % 2 == 0 and x in ne_pov]
    pov= [x for x in a if a.count(x) > 1]
    proiz = 1
    for x in ne_pov:
        proiz *= x
    if n % 2 == 0 and ((len(set(krat))) < len(pov)) and (proiz > sum(pov)):
        c += 1
print(c)