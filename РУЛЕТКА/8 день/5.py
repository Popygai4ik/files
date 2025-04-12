n = list(range(3, 26))
m = list(range(8, 57))
a = list(range(1,100))
for x in range(1,100):
    if (((x in n) <= (x in m)) <= (not(x in a))) == False:
        a.remove(x)
print(a)
