def t34(start, end):

    if start < end:
        return 0
    if start == end:
        return 1
    return t34(start - 3, end) + t34(start // 3, end)
print(t34(81, 27) * t34(27, 3))