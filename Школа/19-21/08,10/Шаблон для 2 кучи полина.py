def f(s1, s2, p, mst):
    if p > mst:
        return False
    if s1 + s2 >= 435:
        return p % 2 == mst % 2

    p +=1
    a = []
    a.append(f(s1 + 1,s2, p, mst))
    a.append(f(s1 * 2, s2,p, mst))
    a.append(f(s1, s2 + 1, p, mst))
    a.append(f(s1, s2 * 2, p, mst))

    if p % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for s in range(1, 210):
    for mst in range(1, 5):
        if f(17, s, 0, mst):
            if mst == 1:
                print(s, mst)
                break
