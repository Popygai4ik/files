# f = open('1.txt')
c = 0
# for s in f:
#     data = list(map(int, s.split()))
#     pov = [x for x in data if data.count(x) > 1]
#     ne_pov = [x for x in data if data.count(x)  == 1]
#     # print(ne_pov, pov)
#     if len(pov) == 4 and len(set(pov)) == 2 and len(ne_pov) == 4:
#         if min(data) in pov:
#             c += 1
# print(c)
# f = open('2.txt')
# c = 0
# for s in f:
#     data = list(map(int, s.split()))
#     # pov = [x for x in data if data.count(x) > 1]
#     # ne_pov = [x for x in data if data.count(x)  == 1]
#     # print(ne_pov, pov)
#     data.sort()
#     if max(data)+min(data)== data[2]+data[1]:
#         if max(data)-min(data)>(data[2]+data[1] - max(data)):
#             c += 1
#
#
# print(c)
f = open('1.txt')
c = 0
for s in f:
    data = list(map(int, s.split()))
    ch = [x for x in data if x%2 == 0]
    ne_ch = [x for x in data if x %2 != 0]
    # print(ne_ch, ch)
    try:
        if max(ne_ch)% 3 == 0:
            if len(ch)% 2 == 0 and len(ne_ch)% 2 ==0:
                c += 1
    except:
        pass


print(c)