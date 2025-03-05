p = list(range(20,150+1))
q = list(range(40,120+1))
r = list(range(30,120+1))
s = list(range(10,80+1))
t = list(range(60,200+1))
u = list(range(90,170+1))
a = []
for x in range(0,1000):
    if ((((x in p) or (x in q)) or ((not(x in a)) <=  ((x in r) and (x in s) or (x in t) and (x in u))))) == False:
        a.append(x)
res = list(range(0,1000))
for j in a:
    res.remove(j)
print(res)
print(len(res))