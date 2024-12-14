def to23(start, stop):
    if start == 20:
        return 0
    if start>stop:
        return 0
    if start == stop:
        return 1
    if start< stop:
        return to23(start +2, stop)+to23(start * 3, stop)
print(to23(2, 24) * to23(24, 100))