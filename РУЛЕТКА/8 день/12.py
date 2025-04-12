from functools import lru_cache

@lru_cache(None)
def to23(start,stop):
    if start < stop:
        return 0
    if start == stop:
        return 1
    if start > stop:
        return to23(start//4,stop) +to23(start - 2,stop) +to23(start - 1,stop)
print(to23(58, 3))
print(to23(58,12)*to23(12,3))
print(to23(58,45)*to23(45,3)*to23(16,12)*to23(12,3))
print(to23(58,41)*to23(41,12) *to23(12,3))
print(to23(58,16)*to23(16,12) *to23(12,3))
166388057304 + 47375998517120+120399516160+121378442360