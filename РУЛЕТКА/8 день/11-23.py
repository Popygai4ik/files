def to23(start, stop):
    if start > stop or start == 35:
        return 0
    if start == stop:
        return 1
    if start < stop:
        return to23(start * 4, stop) + to23(start * 3, stop) + to23(start + 5, stop)
print(to23(5,10)*to23(10,125))