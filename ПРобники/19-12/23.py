def t23(start, stop):
    if start > stop or start == 5:
        return 0
    if start == stop:
        return 1
    if start< stop:
        return t23(start + 1, stop) + t23(start * 3, stop)
print(t23(1, 21))