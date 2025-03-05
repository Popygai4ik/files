print("x y z w f")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (((x and (not(y))) != (w or x)) and (not(z)))
                if f == 0:
                    print(x,y, z, w,f)

'''
x y z w f
0 0 0 1 True
0 1 0 1 True
'''
'''
0 0 1 0 False
0 1 1 1 False
'''
