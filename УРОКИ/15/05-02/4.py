q = list(range(21,57+1))
p = list(range(3,38+1))
a = list(range(1,100))
for x in range(1,100):
    if (((x in q) <= (x in p)) <= (not(x in a))) == False:
        a.remove(x)
print(a)