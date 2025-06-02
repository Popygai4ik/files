print("x y z w f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((w or x) and ((y <= (not(x))) == (x <= z)) and x)
                if f == 1:
                    print(x,y,z,w,f)