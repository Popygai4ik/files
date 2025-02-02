def t23(start, stop):
    if start > stop or start == 21:
        return 0
    if start== stop:
        return 1
    if start<stop:
        return t23(start+3, stop)+t23(start*3,stop)
print(t23(1,10)*t23(10,72))