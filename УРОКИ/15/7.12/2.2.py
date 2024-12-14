# for a in range(1, 10000):
#     for x in range(1, 1000):
#         if (((x & 46 == 0) or (x & 18 == 0)) <= ((x & 115 != 0)  <=(x & a == 0))):
#             break
#     else:
#         print(a)
for a in range(1, 100000):
    for x in range(1, 100000):
        if (((x & 46 == 0) or (x & 18 == 0)) <= ((x & 115 != 0)  <=(x & a == 0))) == False:
            break
    else:
        print(a)