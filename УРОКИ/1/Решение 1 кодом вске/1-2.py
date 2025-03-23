# from itertools import *
# gref = [['А','Г'],['А','Д'],['Г','Д'],['Д','Е'],['Е','Б'],['Е','К'],['К','Б'],['Б','В']]
# table = [[1, 2],[1, 7],
#          [2, 7],
#          [3, 5],[3, 6],
#          [4, 6],
#          [5, 6],[5, 7]]
#
# for var in permutations('АБВГДЕК'):
#     if all(([var[p1 - 1], var[p2-1]] in gref or[var[p2 - 1], var[p1-1]] in gref ) for p1,p2 in table):
#         print([[[k,e]  for k, e in enumerate(var, 1)]])

from itertools import *

graf = [['Б','А'],['Б','Д'],['А','В'],['Д','В'],['В','К'],['В','Е'],['В','Г'],['Г','Е']]
table = [[1,2],[1,4],[2,3],[2 ,6],[2,5],[2,7],[3,6],[4,5]]
for var in permutations('АБВГДЕК'):
    if all(([var[p1 - 1],var[p2 - 1]] in graf or [var[p2 - 1],var[p1 - 1]] in graf)for p1, p2 in table):
        print(*[[[k, e] for k, e in enumerate(var, 1)]])