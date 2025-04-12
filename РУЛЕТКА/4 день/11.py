def t23(start, stop):
    if start == stop:
        return 1
    if start > stop or start == 16:
        return 0
    if start< stop:
        return t23(start + 2, stop) +t23(start* 2, stop) +t23(start * 3, stop)
print(t23(4, 12)*t23(12, 78))