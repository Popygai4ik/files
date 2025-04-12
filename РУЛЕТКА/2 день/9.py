def to23(start, stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    if start< stop:
        return to23(start + 1, stop)  + to23(start * 2, stop)  + to23((start//2) * 5, stop)
print(to23(2, 18)*to23(18,35)*to23(35, 86))
