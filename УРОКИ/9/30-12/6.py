f = open('6.txt')
c = 0
for s in f:
    data = list(map(int, s.split()))
    pov = [x for x in data if data.count(x)  > 1]
    k = 1
    for d in pov:
        k = k * d
    # print(set(data))
    # print(oct(sum(int(i) for i in str(k)) ** 2))
    if len(pov) == 2 and oct(sum(int(i) for i in str(k)) ** 2)[-1] == '0':
        c += 1
print(c)
# s = [1, 1,1,2,5]
# k = 1
# for d in s:
#     k = k * d
# print(k)
# print(''.join(list(map(str, s))))