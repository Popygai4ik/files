# print('x y z w f')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 f = (not(y and (not(w)) and ((not(x)) or z) == (z and (not(y)))))
#                 if f ==1 :
#                     print(x, y, z , w, f)
p = list(range(11, 29))
q = list(range(21, 43))
a = list(range(1, 100))
for x in range(1, 100):
    if (((x in p) == (x in q)) <= (not(x in a))) == False:
        a.remove(x)
print(*a)
