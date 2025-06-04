# 34 - 13
# '''
graf = [['А','Б'],['Б','В'],['Б','Е'],['Б','Ж'],['В','Ж'],['Е','Ж'],['Ж','Г'],['Ж','Д'],['Г','Д'],['Е','Д']]
tables = [[1,4],[1,7],[2,4],[2,6],[3,6],[4,5],[4,6],[4,7],[5,6],[5,7]]
print(len(graf),len(tables))
from itertools import *
for var in permutations('АБВГДЕЖ'):
    if all(([var[p2 - 1], var[p1 - 1]] in graf) or ([var[p1 - 1], var[p2 - 1]] in graf) for p1,p2 in tables):
        print(*[[n+1,e]for n, e in enumerate(var)])
# '''
# 35 - 21
"""

graf = [["А","Б"],["А","Г"],["Б","В"],["В","Г"],["Д","Г"],["Г","Е"],["Е","Ж"],["Г","Ж"]]
tables = [[1,3],[1,7],[2,4],[2,6],[3,4],[3,5],[3,6],[3,7]]
print(len(graf),len(tables))
from itertools import *
for var in permutations('АБВГДЕЖ'):
    if all(([var[p2 - 1], var[p1 - 1]] in graf)or ([var[p1 - 1], var[p2 - 1]] in graf) for p1,p2 in tables):
        print(*[str(str(n+1) +'-'+ str(e))for n, e in enumerate(var)])
"""
# 36 - 65
"""

graf = [["А","Б"],["Б","Г"],["Г","А"],["А","Д"],["Д","Е"],["Д","Л"],["Л","В"],["В","Г"],["В","К"],["К","Е"],["К","И"],["И","Е"]]
tables = [[1,2],[1,6],[1,7],[2,5],[2,9],[3,4],[3,8],[3,9],[4,5],[4,7],[6,7],[8,9]]
print(len(graf),len(tables))
from itertools import *
for var in permutations('АБВГДЕЛКИ'):
    if all( ([var[p2 - 1], var[p1 - 1]] in graf)or ([var[p1 - 1], var[p2 - 1]] in graf)for p1, p2 in tables):
        print(*[str(str(n+1) +'-'+ str(e))for n, e in enumerate(var)])
        1 - А
        2 - Д
        3 - К
        4 - В
        5 - Л
        6 - Б
        7 - Г
        8 - И
        9 - Е
"""
