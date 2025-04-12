def to23(start, stop):
    if start == stop:
        return 1
    if start > stop:
        return 0
    if start<stop:
        s = 0
        for x in range(2,start):
            if start % x == 0:
                s+= x
        if s == 0:
            return to23(start+1, stop)
        else:
            return to23(start + 1, stop)+to23(start + s, stop)

print(to23(2, 56))
