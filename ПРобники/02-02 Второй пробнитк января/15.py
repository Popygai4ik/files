q = list(range(3, 63))
p = list(range(38, 90))
a = []
for x in range(1, 100):
    if (x in a or ((x in q) <= (x in p))) == False:
        a.append(x)
print(*a)
res = 0
# print(a[-1] - a[0])
for c in a:
    if c % 2 == 0:
        res += 1
print(res)