def to23(start, stop, k):
    if start > stop:
        return 0
    if start == stop and k == 2:
        return 1
    else:
        return to23(start + 2, stop, k) + to23(start + 3, stop, k) + to23(start * 2, stop, k + 1) + to23(start * 3, stop, k + 1)
print(to23(1, 51, 0))
