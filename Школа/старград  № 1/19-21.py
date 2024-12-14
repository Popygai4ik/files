def f(s1, p, mst):
    if p > mst:
        return False
    if s1 <= 19:
        return p % 2 == mst % 2

    p +=1
    a = []
    a.append(f(s1 - 1, p, mst))
    if s1 % 3 == 0:
        a.append(f(s1 // 3, p, mst))
    else:
        a.append(f(s1 - 2, p, mst))
    if s1 % 5 == 0:
        a.append(f(s1 // 5, p, mst))
    else:
        a.append(f(s1 - 3, p, mst))

    if p % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for s in range(20, 70):
    for mst in range(1, 5):
        if f(s,  0, mst):
            if mst == 2 or mst== 4:
                print(s, mst)
            break