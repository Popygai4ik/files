q = list(range(10,55+1))
p = list(range(4,20+1))
a = []
for x in range(1, 100):
    if ((x in a) or (((not(x in p)) <= (not(x in q))))) == False:
        a.append(x)
print(a)
