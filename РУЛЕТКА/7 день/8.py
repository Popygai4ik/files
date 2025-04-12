a = [int(s) for s in open('17_2_knCRZiM.txt')]
# def pr(x):
#     if x < 2:
#         return False
#     if x == 2:
#         return True
#     if x % 2 == 0:
#         return False
#     for d in range(3, int(x**0.5)+1, 2):
#         if x % d == 0:
#             return False
#     return True
s_m = [i for i in a if str(i)[-2:] == '25']
r = sum(s_m)/ len(s_m)
print(r)
res = []
for i in range(len(a) - 2):
    n1 = a[i]
    n2 = a[i+1]
    n3 = a[i + 2]
    triple = [n1, n2, n3]
    y1 = any(1000 <= abs(x) <= 9999 for x in triple)
    y2 = ((str(n1)[-2:] == '13') + (str(n2)[-2:] == '13') +(str(n3)[-2:] == '13')) == 2
    y3 = (((n1 > r) + (n2 > r) +(n3 > r) ) == 3)
    if y2 and y1 and y3:
        # print(y1, y2, n1,n2)

        res.append(n1 + n2 + n3)
if res:
        print(len(res), min(res))
else:
    print("✅не найдено.")



# Найти среднее от всех чисел, заканчивающихся на 25
s_m = [i for i in a if str(abs(i))[-2:] == '25']
r = sum(s_m) / len(s_m)

res = []

for i in range(len(a) - 2):
    n1, n2, n3 = a[i], a[i+1], a[i+2]
    triple = [n1, n2, n3]

    # Условие 1: хотя бы одно число четырёхзначное
    y1 = any(1000 <= abs(x) <= 9999 for x in triple)

    # Условие 2: ровно два оканчиваются на '13'
    y2 = sum(str(abs(x))[-2:] == '13' for x in triple) == 2

    # Условие 3: все числа больше среднего r
    y3 = all(x > r for x in triple)

    if y1 and y2 and y3:
        res.append(sum(triple))

if res:
    print(len(res), min(res))
else:
    print("✅ Условию не соответствует ни одна тройка.")
