Q = list(range(20, 40 + 1))
P = list(range(10, 25+1))
A = list()
for x in range(1, 100):
    if (((x in P) and (not(x in Q))) <= (x in A)) == False:
        A.append(x)
print(A)



# for x in range(1, 100):
#     if (((x in a) <= (x in p)) or (x in q)) == False:
#         a.remove(x)
# print(a)
# print(32-13)