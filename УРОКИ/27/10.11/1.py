# f = open('1.txt')
# f.readline()
# points = [list(map(float, s.replace(',', '.').split()))for s in f]
# # print(points)
# min_dis = 10**10
# res = []
# for i in range(len(points) -1 ):
#     for j in range(i + 1, len(points)):
#         centr1 = points[i]
#         centr2 = points[j]
#         dist = 0
#         for pen in points:
#             d1 = ((centr1[0] - pen[0])** 2 + (centr1[1] - pen[1])** 2)**0.5
#             d2 = ((centr2[0] - pen[0]) ** 2 + (centr2[1] - pen[1]) ** 2)**0.5
#             dist += min(d1, d2)
#         if dist< min_dis:
#             min_dis = dist
#             res = [centr1, centr2]
# print(res)
f = open('1.txt')

f.readline()

roots = [list(map(float, s.replace(",", ".").split())) for s in f]

mn = 10**10

ans = []

for i in range(len(roots) - 1):

    for j in range(i + 1, len(roots)):

      a = roots[i]

      b = roots[j]

      s = 0

      for d in roots:

          d1 = ((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2) ** 0.5

          d2 = ((d[0] - b[0]) ** 2 + (d[1] - b[1]) ** 2) ** 0.5

          s += min(d1, d2)

      else:

        if s < mn:

          mn = s

          ans = [a, b]

print(int((ans[0][0] + ans[1][0]) / 2 * 10000), \

      int((ans[0][1] + ans[1][1]) / 2 * 10000))