s = '63 12 93 72 83 19 22'
data = list(map(int, s.split()))
# print(data)
def ost(x):
    return (x % 7)**2
print(sum(map(ost, data)))
print()