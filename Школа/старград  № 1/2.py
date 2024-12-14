print("(x, y, z, w, f)")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                n_w = not w
                f = (not(x) +(not(z) + w)) and (not(z)+ (y == n_w))
                if not f:
                    print(x, y, z, w,  f)
