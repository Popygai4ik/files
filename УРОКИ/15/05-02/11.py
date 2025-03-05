q = list(range(18,32+1))
p = list(range(5, 20+1))
a = list(range(1,100))
for x in range(1, 100):
    if (((x in a) <= (x in p)) or (x in q)) == False:
        a.remove(x)
print(a)