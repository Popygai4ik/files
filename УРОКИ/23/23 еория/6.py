def t23(start, end):
    if start == end:
        return 1
    if start > end:
        return  t23(start -1, end) + t23(start // 3 , end)
    if start< end:
        return 0
print(t23(33, 7) * t23(7, 2))