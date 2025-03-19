# import sys
# g = [0]*50000
# f = [0]*982140
# sys.set_int_max_str_digits(10000)
# for n in range(1,10000):
#     if n == 1:
#         g[n] =1
#     if n >= 2:
#         g[n] = n * g[n - 1]
# for n in range(1,982140):
#     if n <= 7342:
#         f[n] = g[n]
#     elif n > 7342 and n % 2 == 0:
#         f[n] = f[(n // 3) - 278] + n
#     elif n > 7342 and n % 2 != 0:
#         f[n] = f[n - 1] + g[n // 57] + 5
# print(sum(int(i) for i in str(f[982134] - g[241])))
import sys

# Увеличиваем размеры массивов g и f
g = [0] * 50000  # Достаточно для G(n) до 50000
f = [0] * 982140  # Достаточно для F(n) до 982140

# Устанавливаем лимит на максимальное число цифр в int
sys.set_int_max_str_digits(15000)

# Вычисляем G(n)
for n in range(1, 50000):
    if n == 1:
        g[n] = 1
    elif n >= 2:
        g[n] = n * g[n - 1]

# Вычисляем F(n)
for n in range(1, 982140):
    if n <= 7342:
        f[n] = g[n]
    elif n > 7342 and n % 2 == 0:
        f[n] = f[(n // 3) - 278] + n
    elif n > 7342 and n % 2 != 0:
        f[n] = f[n - 1] + g[n // 57] + 5

# Вычисляем сумму цифр выражения F(982134) + G(241)
result = f[982134] + g[241]
sum_of_digits = sum(int(i) for i in str(result))

print(sum_of_digits)
