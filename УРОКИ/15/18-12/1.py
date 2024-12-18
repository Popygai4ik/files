p = list(range(7, 16))
q = list(range(20, 39))
a = list(range(1, 100))
for x in range(1, 100):
    if (((x not in p) <= (x in q)) or (x not in a))  == False:
        a.remove(x)
print(*a)
print(15-7)