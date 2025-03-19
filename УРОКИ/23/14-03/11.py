def t23(start,end):
    if start > end or start == 15:
        return 0
    if start == end:
        return 1
    if start < end:
        return t23(start + 1,end) + t23(start + 2,end)+t23(start * 2,end)

print(t23(4,34))