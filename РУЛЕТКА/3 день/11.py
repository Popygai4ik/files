# a = [int(s) for s in open('11-17')]
# res= []
# def pr(n):
#     n = abs(n)
#     for x in range(2,n):
#         if n % x == 0:
#             return False
#     return True
# def sem(n):
#     n = abs(n)
#     return sum(int(h) for h in str(n))
# def prod(n):
#     n = abs(n)
#     r = 1
#     for h in str(n):
#         r *= int(h)
#     return r
# e = min(a)
# for i in range(len(a)-1):
#     if (bin(abs(a[i]))[-1] != bin(abs(a[i + 1]))[-1]):
#         continue
#     if (sem(a[i])% 2 == 0 and sem(a[i + 1]) % 2 == 0) \
#         and (abs(a[i]) % 7 == 0 and abs(a[i + 1]) % 7 == 0 )\
#         and (not(pr(a[i])) and not(pr(a[i + 1]))) and (abs(prod(a[i]) - prod(a[i + 1])) <= 50)\
#         and (((abs(a[i]) % 8 == 0) + abs(a[i + 1]) % 8 == 0) == 1)
# print(len(res),max(res))
a = [int(s) for s in open('11-17')]  # Читаем данные из файла
res = []


def pr(n):  # Проверка на простоту
    n = abs(n)  # Берём модуль числа, т.к. отрицательные не являются простыми
    if n < 2:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def sem(n):  # Сумма цифр числа
    return sum(int(h) for h in str(abs(n)))  # Берём модуль, чтобы работало с отрицательными числами


def prod(n):  # Произведение цифр числа
    r = 1
    for h in str(abs(n)):  # Берём модуль, чтобы игнорировать знак
        r *= int(h)
    return r


for i in range(len(a) - 1):
    if bin(abs(a[i]))[-1] != bin(abs(a[i + 1]))[-1]:  # Проверка окончания в двоичной системе
        continue
    if sem(a[i]) % 2 != 0 or sem(a[i + 1]) % 2 != 0:  # Сумма цифр каждого из чисел чётная
        continue
    if a[i] % 7 == 0 or a[i + 1] % 7 == 0:  # Оба числа не делятся на 7
        continue
    if pr(a[i]) or pr(a[i + 1]):  # Оба числа не являются простыми
        continue
    if abs(prod(a[i]) - prod(a[i + 1])) > 50:  # Разность произведений цифр не превышает 50
        continue
    if not ((a[i] % 8 == 0 and a[i + 1] % 9 == 0) or (
            a[i] % 9 == 0 and a[i + 1] % 8 == 0)):  # Только одно из чисел делится на 8, а другое на 9
        continue

    res.append(min(a[i], a[i + 1]))

print(len(res), abs(sum(res)), sep='')
# 52158546