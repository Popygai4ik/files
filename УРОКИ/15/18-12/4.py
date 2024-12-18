q = list(range(6, 15))
p = list(range(2, 11))
a = list(range(1, 100))
for x in range(1,100):
    if (((x in a) <=(x in p)) or (x in q)) == False:
        a.remove(x)
print(*a)

            