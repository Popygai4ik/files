p = list(range(20,130+1))
q = list(range(40,100+1))
r = list(range(30,120+1))
s = list(range(50,150+1))
a = []
for x in range(1, 200):
    if ((((x in p) or (x in q)) and ((not(x in a)) or (x in r))) <= (x in s)) == False:
        a.append(x)

print(a)