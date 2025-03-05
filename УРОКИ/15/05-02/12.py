q = list(range(33, 88+1))
p = list(range(10, 49+1))
a = list(range(1, 100+1))
for x in range(1,100+1):
    if (((x in p) <= (not(x in q))) <= (not(x in a))) == False:
        a.remove(x)
print(a)