from reportlab.lib.normalDate import bigBang


def dell(n,m):
    return n % m == 0

# for a in range(1,1000):
#     for x in range(1,1000):
#         if ((dell(x,a) and (not(dell(x,12)))) <= (not(dell(x,18)))) == False:
#             break
#     else:
#         print(a)

# for a in range(1,1000):
#     for x in range(1,5000):
#         if ((dell(x,a) and (dell(x,8))) <= (((not(dell(x,8))) or dell(x,240)))) == False:
#             break
#     else:
#         print(a)
# for a in range(1,1000):
#     for x in range(1,5000):
#         if ((not(dell(x,a))) <= (dell(x,15) <= (not(dell(x,9))))) == False:
#             break
#     else:
#         print(a)
# for a in range(1,1000):
#     for x in range(1,5000):
#         if ((((dell(x,24) and dell(x,36)) <= dell(x,a)) and (a ** 2 - a - 5000 < 112))) == False:
#             break
#     else:
#         print(a)
# for a in range(1,1000):
#     for x in range(1,5000):
#         if ((x & 17 == 0) <= ((x & 37 == 0) or (x & a != 0))) == False:
#             break
#     else:
#         print(a)
#
# for a in range(1,1000):
#     for x in range(1,5000):
#         if ((x & a != 0) <= (((x & 76 == 0) or (x & 45 == 0) ) <= (x & 22 != 0))) == False:
#             break
#     else:
#         print(a);
# for a in range(0,1000):
#     for x in range(1,5000):
#         for y in range(1,5000):
#             if (((2 * y + 3 * x) <a) or (x > 15) or (y > 35)) == False:
#
#                 break
#         if (((2 * y + 3 * x )< a) or (x > 15) or (y > 35)) == False:
#             break
#     else:
#         print(a)
# for a in range(1,1000):
#     for x in range(1,2500):
#         for y in range(1,2500):
#             if ((((y + 5* x) != 31) or (a > (x - 2))) and (a < (y + 37))) == False:
#                 break
#         if ((((y + 5 * x) != 31) or (a > (x - 2))) and (a < (y + 37))) == False:
#             break
#     else:
#         print(a)
# for a in range(0,1000):
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if ((x > a) or (y > a) or ((y - 2*x + 16) != 0)) == False:
#                 break
#         if ((x > a) or (y > a) or ((y - 2 * x + 16) != 0)) == False:
#             break
#     else:
#         print(a)
# for a in range(0, 1000):
#     for x in range(1,500):
#         for y in range(1,500):
#             for z in range(1,500):
#                 if (((x + y) < 10) or ((2 * y + x)>50) or ((2 * z - x) < a) or ((4 * y - z) < 40))  == False:
#                     break
#
#             if (((x + y) < 10) or ((2 * y + x) > 50) or ((2 * z - x) < a) or ((4 * y - z) < 40)) == False:
#                 break
#         if (((x + y) < 10) or ((2 * y + x) > 50) or ((2 * z - x) < a) or ((4 * y - z) < 40)) == False:
#             print(a,'-')
#             break
#
#     else:
#         print(a)
# for a in range(1,1000):
#     for x in range(1,5000):
#         if ((x * a > 1138) or (dell(x,3) <= (not(dell(x,7))))) == False:
#             break
#     else:
#         print(a)
# q = list(range(10,55 + 1))
# p = list(range(4,20 + 1))
# a = []
# for x in range(0,100):
#     if ((x in a) or ((not(x in p)) <= (not(x in q)))) == False:
#         a.append(x)
# # print(a)
# q = list(range(33, 88 + 1))
# p = list(range(10,49 + 1))
# a = list(range(0,100))
# for x in range(0,100):
#     if (((x in p) <= (not(x in q))) <= (not(x in a))) == False:
#         a.remove(x)
# print(a)
# q = list(range(21,57+ 1))
# p = list(range(3,38 + 1))
# a = list(range(1,100))
# for x in range(1,100):
#     if (((x in q) <= (x in p)) <= (not(x in a))) == False:
#         a.remove(x)
# print(a)
# p = list(range(27,130 + 1))
# q= list(range(50,62 + 1))
# r = list(range(38,94 + 1))
# a = []
# for x in range(1,200):
#     if (((x not in p) or (x in q)) or ((not(x in a)) <= (not(x in r)))) == False:
#         a.append(x)
# print(a)
# b = list(range(45,90 + 1))
# res = []
# for a in range(1,1000):
#     for x in range(1,1000):
#         if (dell(x,52) and  (not((not(x in b)) or dell(x,a)))) == True:
#             break
#     else:
#         res.append(a)
# # print(len(res))
# p = list(range(20,130 + 1))
# q = list(range(40, 100 + 1))
# r = list(range(25,120 + 1))
# s = list(range(50, 150 + 1))
# a = []
# for x in range(1,200):
#     if ((((x in p) or (x in q)) and ((not(x in a)) and (x in r))) <= (x in s)) == False:
#         a.append(x)
# print(a)

b = list(range(70, 90 + 1))
for a in range(1,1000):
    for x in range(1,1000):
        if (dell(x,a) or ((x in b) <= (not(dell(x,27))))) == False:
            break
    else:
        print(a)