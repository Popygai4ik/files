from math import sqrt

s = '49 121 25 64 9 16 81 144 144 9 100 1024 25 49 49'

def res(x):
    return sqrt(x) * 4

d = list(map(int, s.split()))

print(sum(map(res, d)))
