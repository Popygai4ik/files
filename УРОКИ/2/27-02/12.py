print("x y z w k f")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                for k in range(2):
                    f = ((x or y) and (w or z)) or ((k and(not (x))) or ((not(y)) and  z))and ((not(w)) or k)
                    if f == 0:
                        print(x,y, z, w, k, f)
'''
x y z w k f
0 0 0 1 0 0
0 0 1 1 0 0
0 1 0 0 0 0
1 0 0 0 0 0
1 0 0 0 1 0
1 1 0 0 0 0
1 1 0 0 1 0
'''