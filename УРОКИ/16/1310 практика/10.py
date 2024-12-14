def t34(start, end):
    if start == 35:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    return t34(start+ 1, end) + t34(start * 3, end) +t34(start * 4, end)
print(t34(3, 10) * t34(10, 70))