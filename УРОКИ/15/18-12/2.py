r = list(range(35, 51))
q = list(range(5, 16))
p = list(range(10, 41))
a = []
for x in range(1, 100):
    if (((x in a) or (x in p)) or ((x in q) <= (x in r))) == False:
        a.append(x)
print(*a)