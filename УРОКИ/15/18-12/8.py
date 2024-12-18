D = list(range(28, 70))
c = list(range(40, 92))
a = []
# for x in range(1, 100):
#     if ((x in D) <= (not(x in c) and not(x in a)) <= (not(x in D))) == False:
#         # a.append(x)
# print(*a)
# print(69-28)
for x in range(1, 100):
    if (((x in D) <= ((x not in c) and (x not in a))) <= (x not in D)) == False:
        a.append(x)
print(*a)