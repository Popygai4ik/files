# def f(x,y,z,w):
#     return (x and (not(w)) and (y or (not(z))))
# table = [(0,0,0,1),(0,1,0,1),(0,1,1,1)]
# for i in permutations('xyzw'):
#     if [f(**dict(zip(i,stroka))) for stroka in table] == [1,1,1]:
#         print(i)
# for x in range()
#
# def f(x,y,z,w):
#     return (((y <= x) == (w <= (not(z)))) and (w or x))
#
# for a in product([0,1], repeat=2):
#     table = [(0,1,1,1),(1,0,1,0),(a[0],0,0,a[1])]
#     if len(set(table)) != 3:
#         continue
#     for i in permutations('xyzw'):
#         if [f(**dict(zip(i,stroka))) for stroka in table] == [0,1,1]:
#             print(i)
# print('x y z w f1 f2')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 =((w or x) and ((y <= (not(x))) == (x <= z)) and x )
#                 if f1 == 1:
#                     print(x,y,z, w,int(f1))
'''
("\n"
 "x y z w f1 f2\n"
 "0 0 0 1 0 0\n"
 "0 0 1 1 1 0\n"
 "0 1 0 0 0 1\n"
 "0 1 0 1 1 0\n"
 "\n"
 "\n"
 "\n"
 "\n"
 "\n"
 "\n"
 "1 1 0 0 1 0\n"
 "1 1 0 1 0 0\n"
 "1 1 1 0 1 0\n"
 "1 1 1 1 1 0\n"
'''
from itertools import *

# def f(x,y,z,w):
#     return (((z <= y) == (x <= (not(w)))) and (x or y))
# for a in product([0,1], repeat=2):
#     table = [(0,1,1,1),(1,0,1,0),(a[0],0,0,a[1])]
#     if len(set(table)) != 3:
#         continue
#     for i in permutations('xyzw'):
#         if [f(**dict(zip(i, st))) for st in table] == [0,1,1]:
#             print(i)
print('x y w z f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (((x <= y) <= z) or (not(w)))
                if f == 0:
                    print(x,y,w,z,f)