r = list(range(12, 30+1))
q = list(range(8,15+1))
p = list(range(10, 20+1))
a = []
for x in range(1,100):
    if (((x in a) or (x in p)) or ((x in q) <= (x in r))) == False:
        a.append(x)

print(a)