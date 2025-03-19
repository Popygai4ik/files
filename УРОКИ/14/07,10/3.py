s = 1024**789 + 256**678 - 64**567
def to_5(s):
    res = ''
    while s > 0:
        res += str(s % 5)
        s = s // 5
    return res[::-1]
print(to_5(s).count('4'))