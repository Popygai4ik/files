# # n = int(input())
# # a = []
# # for i in range(n):
# #     a.append(int(input()))
# # c = 0
# # for i in a:
# #     i = int(i)
# #     if i % 10 == 8 and i % 6 == 0:
# #         c += 1
# # print(c)
# from  functools import lru_cache
# def moves(h):
#     return h + 1, h * 2
# @lru_cache(None)
# def game(h):
#     if h >= 129:
#         return "W"
#     if any(game(m) == "W" for m in moves(h)):
#         return "P1"
#     if all(game(m) == "P1" for m in moves(h)):
#         return "B1"
#     if any(game(m) == "B1" for m in moves(h)):
#         return "P2"
#     if all(game(m) == "P1" or game(m) == "P2" for m in moves(h)):
#         return "B2"
# for s in range(1, 128):
#     if game(s) == "B2":
#         print(s, game(s))
# vod = []
# rezni = 0
# for i in range(4):
#     if i != 3:
#         vod.append(int(input()))
#     else:
#         rezni = int(input())
# vod.sort()
# mini1 = vod[0]
# sredni_tolsi = vod[1]
# boss_kfss = vod[2]
# raznitsa_ = abs(mini1 + sredni_tolsi - boss_kfss)
# print(max(0, raznitsa_ - rezni))
#
# # Считываем входные значения
vod = []
for i in range(5):
    vod.append(int(input()))
h, a, x, b_werwerwe, i = vod

# Обмен значениями, если x < i
if x < i:
    a, b_werwerwe = b_werwerwe, a
    x, i = i, x

# Проверка условия
if a * (2 * x + 1) + b_werwerwe * (2 * i + 1) < h:
    print(-1)
else:
    n1, n2, ind = 0, 0, 1
    ans = []

    # Основной цикл
    while ind < h + 1 and n1 <= a and n2 <= b_werwerwe:
        if n1 < a:
            if ind + x <= h:
                ind += x
            ans.append((ind, x))
            ind += x + 1
            n1 += 1
        else:
            if ind + i <= h:
                ind += i
            ans.append((ind, i))
            ind += i + 1
            n2 += 1

    # Вывод результатов
    if ind >= h:
        for p in ans:
            print(p[0], p[1])
    else:
        print(-1)
# import sys
# s = int(input())
# n = int(input())
# a = [[int(input()), i+1 ]for i in range(n)]
# # print(a)
# f = s
# u = 0
# for j in range(len(a)):
#     e, i = a[j]
#     if i > f and a[j][0] >= 0:
#         break
#     elif i > f and e <= 0:
#         continue
#     (u, f) = (a[j][1], f + e) if f + a[j][0] >= f else (u, f)
# print((f - n - 1) % (f - n))
#
# nachalnaya_energia = int(input())
# kolvo_kochek = int(input())
#
# energiya_na_kochkakh = [[int(input()), i + 1] for i in range(kolvo_kochek)]
#
# tekushaya_energiya = nachalnaya_energia
# last_poziciya = 0
#
# for energiya, kachka in energiya_na_kochkakh:
#     if kachka > tekushaya_energiya and energiya >= 0:
#         break
#     elif kachka > tekushaya_energiya and energiya <= 0:
#         continue
#     if tekushaya_energiya + energiya >= tekushaya_energiya:
#         last_poziciya, tekushaya_energiya = kachka, tekushaya_energiya + energiya
#
#
# print((tekushaya_energiya - kolvo_kochek - 1) % (tekushaya_energiya -
# vod = []
# for i in range(3):
#     vod.append(int(input()))
# m, n, k = vod
# ans = 0
#
# # Перебор для n
# for i in range(1, n + 1):
#     l, r = 0, m + 1
#     while r - l > 1:
#         mid = (r + l) // 2
#         if n * m - i * mid >= k - 1:
#             l = mid
#         else:
#             r = mid
#     ans = max(ans, l * i)
#
# # Перебор для m
# for i in range(1, m + 1):
#     l, r = 0, n + 1
#     while r - l > 1:
#         mid = (r + l) // 2
#         if n * m - i * mid >= k - 1:
#             l = mid
#         else:
#             r = mid
#     ans = max(ans, l * i)
#
# print(ans)

# razmer_po_verti = int(input())
# razmer_po_gorzinle= int(input())
# kolvo_kuskov = int(input())
#
# maksimalny_jopa_sholada = 0
#
#
# for kysashek in range(1, razmer_po_gorzinle + 1):
#     leva_granica, prava_granica = 0, razmer_po_verti + 1
#     while prava_granica - leva_granica > 1:
#         ceredne = (prava_granica + leva_granica) // 2
#
#         if razmer_po_gorzinle * razmer_po_verti - kysashek * ceredne >= kolvo_kuskov - 1:
#             leva_granica = ceredne
#         else:
#             prava_granica = ceredne
#     maksimalny_jopa_sholada = max(maksimalny_jopa_sholada, leva_granica * kysashek)
#
#
# for kysashek in range(1, razmer_po_verti + 1):
#     leva_granica, prava_granica = 0, razmer_po_gorzinle + 1
#     while prava_granica - leva_granica > 1:
#         ceredne = (prava_granica + leva_granica) // 2
#         if razmer_po_gorzinle * razmer_po_verti - kysashek * ceredne >= kolvo_kuskov - 1:
#             leva_granica = ceredne
#         else:
#             prava_granica = ceredne
#     maksimalny_jopa_sholada = max(maksimalny_jopa_sholada, leva_granica * kysashek)
#
#
# # print(maksimalny_jopa_sholada)
# N = int(input())
# A = int(input())
# X = int(input())
# B = int(input())
# Y = int(input())
#
# if X >= Y:
#     R1, C1 = X, A
#     R2, C2 = Y, B
# else:
#     R1, C1 = Y, B
#     R2, C2 = X, A
#
# s = 1  # Start from the first house
# lamps = []
#
# while s <= N:
#     if C1 > 0:
#         p = min(N, s + R1)
#         lamps.append((p, R1))
#         C1 -= 1
#         r = min(N, p + R1)
#         s = r + 1
#     elif C2 > 0:
#         p = min(N, s + R2)
#         lamps.append((p, R2))
#         C2 -= 1
#         r = min(N, p + R2)
#         s = r + 1
#     else:
#         print(-1)
#         exit()
#
# for lamp in lamps:
#     print(f"{lamp[0]} {lamp[1]}")
# vod = []
# for _ in range(5):
#     vod.append(int(input()))
#
# visota, paramewrwerwe_A, multiplieqweqwewqr_X, jkopa_B, qweqwe = vod
#
# if multiplieqweqwewqr_X < qweqwe:
#     paramewrwerwe_A, jkopa_B = jkopa_B, paramewrwerwe_A
#     multiplieqweqwewqr_X, qweqwe = qweqwe, multiplieqweqwewqr_X
#
# if paramewrwerwe_A * (2 * multiplieqweqwewqr_X + 1) + jkopa_B * (2 * qweqwe + 1) < visota:
#     print(-1)
# else:
#     count_A, count_B, current_index = 0, 0, 1
#     atvet = []
#
#     while current_index < visota + 1 and count_A <= paramewrwerwe_A and count_B <= jkopa_B:
#         if count_A < paramewrwerwe_A:
#             if current_index + multiplieqweqwewqr_X <= visota:
#                 current_index += multiplieqweqwewqr_X
#             atvet.append((current_index, multiplieqweqwewqr_X))
#             current_index += multiplieqweqwewqr_X + 1
#             count_A += 1
#         else:
#             if current_index + qweqwe <= visota:
#                 current_index += qweqwe
#             atvet.append((current_index, qweqwe))
#             current_index += qweqwe + 1
#             count_B += 1
#
#     if current_index >= visota:
#         for position, step in atvet:
#             print(position, step)
#     else:
#         print(-1)
from itertools import product

b_werwerwe = int(input())
ndsfsdf = int(input())
werrwe = int(input())

masks = []
sums = []

for _ in range(werrwe):
    masks.append(input().strip())
    sums.append(int(input().strip()))

def proverka_parile(code):
    for mask, required_sum in zip(masks, sums):
        total_sum = sum(int(code[i]) for i in range(ndsfsdf) if mask[i] == '1')
        if total_sum != required_sum:
            return False
    return True

podhodit = 0
for code in product(range(b_werwerwe), repeat=ndsfsdf):
    if proverka_parile(code):
        podhodit += 1

print(podhodit)
