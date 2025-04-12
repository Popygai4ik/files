def t23(start, stop):
    if start == stop:
        return 1
    elif start > stop or start == 10 or start == 15:
        return 0
    elif start< stop:
        return t23(start + 1 ,stop) + t23(start * 2 ,stop) + t23(start * 3,stop)
print(t23(2,12)*t23(12,55))
