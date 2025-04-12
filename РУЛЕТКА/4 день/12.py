def t23(start, stop):
    if start > stop or start == 60:
        return 0
    if start == stop:
        return 1
    if start < stop:
        return t23(start+ 4, stop) +t23(start+ 3 , stop) +t23(start + 2, stop)
print(t23(56, 86))