def t23(start, end):
    if start == 30:
        return 0
    if start == end:
        return 1
    if start > end:
        return 0
    if start< end:
        return t23(start +1, end) + t23(start * 3, end)
print(t23(3, 20) * t23(20, 80))