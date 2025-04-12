L = list(range(9, 21))
N = list(range(6, 27))
F = list(range(4, 39))
o = [9, 10]
for x in range(1,100):
    if ((((not((x * 2) in L)) )and (x in N)) <= ((not(x in F)) or (x in o))) == False:
        o.append(x)
print(o)

print(len(o))