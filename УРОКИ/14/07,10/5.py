s =  5**172 + 4**347 - 8**93
def to_4(s):
    res = ''
    while s > 0:
        res += str(s % 4)
        s = s // 4
    return res[::-1]
sh = to_4(s).count('0')
print(oct(sh))