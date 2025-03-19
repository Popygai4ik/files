def to23(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    if start > end:
        return to23(start-1, end) + to23(start // 2, end)+ to23(start//3, end)
print(to23(20, 9)*to23(9, 1))