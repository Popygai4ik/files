def t34(start, end):
    if start == 23:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    return t34(start+ 1, end) + t34(start * 2, end)
print(t34(4, 66) * t34(66, 93))