def to23(start, end):
    if start > end:
        return  0
    if start == end:
        return 1
    return to23(start + 1, end) + to23(int('1' + bin(start)[2:], 2), end)
print(to23(1,int('1111011', 2)))