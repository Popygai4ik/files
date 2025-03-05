p = list(range(27, 130+1))
q = list(range(50, 62+1))
r = list(range(38,94+1))
a = []
for x in range(1, 100):
    if (((x not in p) or (x in q)) or ((not(x in a)) <= (not(x in r)))) == False:
        a.append(x)
print(a)