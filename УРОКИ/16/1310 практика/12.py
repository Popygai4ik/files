def t34(start, end):

    if start < end:
        return 0
    if start == end:
        return 1
    return t34(start - 1, end) + t34(start // 3, end)+ t34(start // 2, end)
print(t34(131, 41) * t34(41, 3))