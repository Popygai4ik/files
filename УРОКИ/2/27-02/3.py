print("x y z w f")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (((w <= y) and z) or (not(x)))
                if f == 1:
                    print(x,y, z, w,f)

'''
1 0 0 1 False
1 0 1 1 False
1 1 0 1 False
x y z w f
1 0 0 0 False
1 1 0 0 False
'''
'''
1 1 1 0 1


0 1 1 1 1

'''