q = list(range(18, 35))
p = list(range(2, 17))
a = []
for x in range(1, 100):
    if (((x in p) or(x in q)) <= (x in a)) == False:
        a.append(x)

print(*a)
print(34-2)