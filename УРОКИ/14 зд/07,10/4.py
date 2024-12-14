s= 1296**625 * 216**125 + 36**25 - 6**5
def to_6(s):
    res = ''
    while s >0:
        res += str(s % 6)
        s = s // 6
    return res[::-1]
print(to_6(s).count('5'))