def t34(start, end):
    if start == 5:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    return t34(start+ 1, end) + t34(start * 3, end)
print(t34(1, 21))