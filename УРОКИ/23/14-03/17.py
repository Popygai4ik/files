def to23(start, stop):
    if start < stop:
        return 0
    if start == stop:
        return 1
    return to23(start - 2, stop) +to23(start // 3, stop)+to23(int(oct(start//4)[2:]), stop)
print(to23(98, 56)*to23(56,11))