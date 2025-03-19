import sys

# sys.setrecursionlimit(25000)
def to23(start, stop, p):
    if start - 1 > stop or '****' in p or '--'  in p:
        return 0
    if start == stop:
        return 1
    return to23(start - 1, stop, p + '-') +  to23(start * 2, stop, p + '*') +  to23(start * 3, stop, p + '*')
print(to23(4,116, ''))
