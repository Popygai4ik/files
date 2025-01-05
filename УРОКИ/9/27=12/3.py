f = open('2.txt')
# c = 0
# for s in f:
#     a = list(map(int, s.split()))
#     pov = []
#     for x in a:
#         if a.count(x) > 1:
#             pov.append(x)
#     ne_pov = []
#     for x in a:
#         if a.count(x) == 1:
#             ne_pov.append(x)
#     if len(set(a)) < 6 and sum(ne_pov) % 2 != 0:
#         c += 1
# print(c)
cnt = 0

for i in f:

    s = list(map(int, i.split()))

    if len(set(s)) <= 5:

        repeat_elem = []

        for q in s:

            if s.count(q) >= 2:

                repeat_elem.append(q)

        set_s = sum(s) - sum(repeat_elem)

        if set_s % 2 != 0:

            cnt += 1

print(cnt)