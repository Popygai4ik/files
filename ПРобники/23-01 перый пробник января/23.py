def t23(start, stop):
    if start > stop or start == 26:
        return 0
    if start == stop:
        return 1
    if start< stop:
        return t23(start+2, stop) + t23(start*2, stop)
print(t23(2, 14)*t23(14, 56))