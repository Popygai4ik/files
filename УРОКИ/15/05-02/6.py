q = list(range(18,30+1))
p = list(range(5,16 + 1 ))
a = []
for x in range(1,100):
    if (((x in p) or ( x in q)) <= (x in a)) == False:
        a.append(x)
print(a)