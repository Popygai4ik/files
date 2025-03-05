P = list(range(6, 17))
Q = list(range(7, 16))
A = list()
for x in range(1, 100):
    if ( ((x in P) or not(x in A)) and  (not(x in Q) or (x in A))) == False:
        A.append(x)
print(A)

print(16-7)




# for x in range(1, 100):
#     if (((x in a) <= (x in p)) or (x in q)) == False:
#         a.remove(x)
# print(a)
# print(32-13)