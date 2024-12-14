def t23(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    if start< end:
        return t23(start +2, end) + t23(start * 3, end) + t23(start ** 2 , end)
print(t23(3, 77))