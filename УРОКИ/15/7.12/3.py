# for a in range(1, 10000):
#     for x in range(1, 10000):
#         if ((x & 15 != 0) or (x & 34 == 0) or (x & a != 0)) == False:
#             break
#     else:
#         print(a)
def f(s, c):
    if s > c or s == 13:
        return 0
    elif s == c:
        return 1
    return f(s+1, c)+f(s+2, c)+f(s*3, c)
print(f(3, 8)*f(8,18))