def to_5(s):
    res = ''
    while s > 0:
        res += str(s % 5)
        s = s // 5
    return res[::-1]
s =  35**28 + 92**15 - 12**5
pet = to_5(s).count('3')
def to_9(s):
    res = ''
    while s > 0:
        res += str(s % 9)
        s = s // 9
    return res[::-1]
print(to_9(pet))