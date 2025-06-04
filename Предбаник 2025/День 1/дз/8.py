# table = [[1,2],[1,4],[2,3],[2,5],[2,6],[2,7],[3,6],[4,5]]
# graf = [["А","Б"],["А","В"],["В","Д"],["Б","Д"],["В","Е"],["В","Г"],["Е","Г"],["В","К"]]
# print(len(table),len(graf))
# from itertools import *
# for var in permutations('АБВГДЕК'):
#     if all(([var[p2 - 1], var[p1 - 1]] in graf or [var[p1 - 1], var[p2 - 1]] in graf)for p1,p2 in table):
#         print(*[str(n)+" - "+str(e + 1) for e,n in enumerate(var)])

# tables = [[1,2],[1,4],[1,6],[2,3],[2,4],[2,5],[2,7],[3,5],[3,7],[4,6],[4,7],[6,7]]
# graf = [["А","В"],["А","Б"],["А","Г"],["Г","Б"],["Г","В"],["Г","Д"],["Г","К"],["В","Е"],["В","Д"],["Д","К"],["Д","Е"],["Е","К"]]
# print(len(tables),len(graf))
# from itertools import *
# for var in permutations('АБВГДЕК'):
#     if all(([var[p2 - 1], var[p1 - 1]] in graf or [var[p1 - 1], var[p2 - 1]] in graf)for p1,p2 in tables):
#         print(*[str(n) + " - " + str(e + 1) for e, n in enumerate(var)])

# tables = [[1,3],[1,5],[1,8],[2,6],[2,7],[2,8],[3,4],[3,5],[4,5],[4,7],[5,7],[6,7],[7,8]]
#
# graf = [["А","Б"],["А","З"],["Б","З"],["З","Г"],["З","Д"],["Б","Г"],["Д","В"],["А","В"],["В","Ж"],["Ж","Е"],["Е","Д"],["Д","Г"],["Д","Ж"]]
#
# print(len(tables),len(graf))
# from itertools import *
# for var in permutations('АБВГДЕЖЗ'):
#     if all(([var[p2 - 1], var[p1 - 1]] in graf or [var[p1 - 1], var[p2 - 1]] in graf)for p1,p2 in tables):
#         print(*[str(n) + " - " + str(e + 1) for e, n in enumerate(var)])
# tables = [[1,2],[1,3],[1,4],[1,7],[2,4],[3,4],[4,5],[4,6],[5,7],[6,7]]
#
# graf = [["C","B"],["C","A"],["A","D"],["D","B"],["C","D"],["D","H"],["D","E"],["E","F"],["H","F"],["C","F"]]
# print(len(tables),len(graf))
# from itertools import *
# for var in permutations('ABCDEFH'):
#     if all(([var[p2 - 1], var[p1 - 1]] in graf or [var[p1 - 1], var[p2 - 1]] in graf)for p1,p2 in tables):
#         print(*[str(n) + " - " + str(e + 1) for e, n in enumerate(var)])

# tables = [[1,5],[1,7],[2,3],[2,6],[2,7],[3,6],[4,6],[4,7],[5,6],[5,7]]
#
# graf = [["В","Е"],["В","А"],["Е","А"],["Е","Г"],["Е","Ж"],["Г","Б"],["А","Б"],["Б","Д"],["Д","Ж"],["Б","Ж"]]
# print(len(tables),len(graf))
# from itertools import *
# for var in permutations('АБВГДЕЖ'):
#     if all(([var[p2 - 1], var[p1 - 1]] in graf or [var[p1 - 1], var[p2 - 1]] in graf)for p1,p2 in tables):
#         print(*[str(n) + " - " + str(e + 1) for e, n in enumerate(var)])
tables = [[1,2],[1,3],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[3,7],[4,5],[4,8],[6,8]]
graf = [["A","B"],["B","C"],["A","C"],["A","D"],["A","E"],["A","F"],["A","G"],["A","H"],["C","D"],["E","F"],["F","G"],["G","H"]]
print(len(tables),len(graf))
from itertools import *
for var in permutations('ABCDEFHG'):
    if all(([var[p2 - 1], var[p1 - 1]] in graf or [var[p1 - 1], var[p2 - 1]] in graf)for p1,p2 in tables):
        print(*[str(n) + " - " + str(e + 1) for e, n in enumerate(var)])
        """
        
B - 1 A - 2 C - 3 G - 4 H - 5 E - 6 D - 7 F - 8
D - 1 A - 2 C - 3 F - 4 E - 5 H - 6 B - 7 G - 8
D - 1 A - 2 C - 3 G - 4 H - 5 E - 6 B - 7 F - 8"""