p = list(range(13, 37))
q = list(range(22, 51))
def Del(n, m):
    return n %  m == 0

a = []
for x in range(1, 100):
    if (((x in q) <= (Del(x, 18) or (x in p))) <= (x in a)) == True:
        a.append(x)
print(*a)
print(51-37)