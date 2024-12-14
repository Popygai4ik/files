from string import *
x = 456223 + 77707 - 51249
print(x)
ascii_uppercase = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def to_25(s):
    x25 = ""
    while s> 0:
        x25 += str(ascii_uppercase[s % 25])
        s = s // 25
    return x25[::-1]
print(to_25(x))

