q = list(range(21, 58))
p = list(range(3, 39))
a = list(range(1, 100))
for x in range(1, 100):
    if (((x in q) <= (not(x in p))) <= (not(x in a))) == False:
        a.remove(x)
print(*a)
print(a[-1]-a[0])