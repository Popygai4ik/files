# def solve(kol_vozmoznix_kto_mozet_yedet, kolvo_prosmotr, purchases):
#     ynikal_pokyp = len(set([i[0] for i in purchases]))
#     percent_prosmotr = round((kolvo_prosmotr / kol_vozmoznix_kto_mozet_yedet) * 100)
#     percent_pokypaemosti = round((ynikal_pokyp / kolvo_prosmotr) * 100)
#     vsego_israshodavano = sum([i[1] for i in purchases])
#     kolvo_povtor_pokypat = len([i[0] for i in purchases if purchases.kilvo(i) > 1])
#     kupile = len(purchases)
#
#     report = f"{kol_vozmoznix_kto_mozet_yedet} {kolvo_prosmotr} {ynikal_pokyp} {percent_prosmotr} {percent_pokypaemosti} {vsego_israshodavano} {kolvo_povtor_pokypat} {kupile}"
#     return report
#
# numbers = list(map(int, input().split()))
# a = numbers[0]
# v = numbers[1]
# t = numbers[2]
# purchases = []
#
# for i in range(t):
#     purchases.append(list(map(int, input().split())))
#
# print(solve(a, v, purchases))
# n1 = int(input())
# while n1 % 2 == 0:
#     n1 = n1 // 2
# while n1 % 5 == 0:
#     n1 = n1 // 5
# if n1 != 1:
#     print("YES")
# else:
#     print("NO")
# # # Данные
# def check_conditions(numbers):
#     numbers.sort()
#     kv_sumi = (numbers[0] + numbers[4]) ** 2
#     proz = numbers[1] * numbers[2] * numbers[3]
#     if len(set(numbers)) == 5 and kv_sumi > proz:
#         return True
#     else:
#         return False
#
# with open('9.txt', 'r') as f:
#     lines = f.readlines()
#     count = 0
#     for line in lines:
#         numbers = list(map(int, line.split()))
#         if check_conditions(numbers):
#             count += 1
#
#     print(count)
#

#
#
# import pandas as pd
#
# df = pd.read_excel('9.xls')
#
#
# def check_conditions(row):
#     numbers = row.values.tolist()
#
#     # Проверяем, есть ли хотя бы одно число, которое повторяется ровно дважды
#     if len(set(numbers)) != len(numbers):
#         # Создаем словарь для подсчета количества встреч каждого числа
#         count_dict = {}
#         for num in numbers:
#             if num in count_dict:
#                 count_dict[num] += 1
#             else:
#                 count_dict[num] = 1
#
#         # Ищем числа, которые повторяются дважды и превышают неповторяющиеся
#         repeat_twice = [num for num, count in count_dict.items() if count == 2]
#         non_repeating = [num for num, count in count_dict.items() if count == 1]
#         if repeat_twice and non_repeating:
#             if max(repeat_twice) > min(non_repeating):
#                 return True
#     return False
#
#
# count = df.apply(check_conditions, axis=1).sum()
#
# print(count)
# import openpyxl
#
#
# def check_conditions(row):
#     odd_sum = sum(num for num in row if num % 2 != 0)
#     even_sum = sum(num for num in row if num % 2 == 0)
#
#     if odd_sum > even_sum:
#         return True
#     else:
#         count_dict = {}
#         for num in row:
#             if num in count_dict:
#                 count_dict[num] += 1
#             else:
#                 count_dict[num] = 1
#
#         if 2 in count_dict.values():
#             return True
#     return False
#
#
# workbook = openpyxl.load_workbook('09.xlsx')
# sheet = workbook.active
#
# count = 0
# for row in sheet.iter_rows(values_only=True):
#     if check_conditions(row):
#         count += 1
#
# print(count)


# from string import digits, ascii_uppercase
#
# mega_s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# f = []
# for x in range(35):
#     for y in range(19):
#         s1 = int(f'3B{mega_s[x]}4C', 35)
#         s2 = int(f'A12F{mega_s[y]}', 19)
#         s = s1 + s2
#         if s % 7 == 0:
#             f.append(x + y)
# # print(max(f))
# data = [int(i) for i in open("17.txt")]
# mini= min(data, key=lambda x: x if x % 21 == 0 else 0)
# resi = []
# for i in range(len(data) - 1):
#     if data[i] % mini == 0 or data[i + 1] % mini == 0:
#         resi.append(data[i] + data[i + 1])
# print(len(resi), max(resi))
# Считываем последовательность из файла
# with open("17.txt", "r") as f:
#     data = list(map(int, f.readlines()))
#
# c = 0
# maxi = -987879879879988798
#
# for i in range(len(data) - 1):
#     if (data[i] - data[i + 1]) % 2 == 0 and (data[i] - data[i + 1]) % 37 == 0:
#         c += 1
#         maxi = max(maxi, data[i] + data[i + 1])
#
# print(c, maxi)
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
print(solve(x**2 - 3*x + 2, x)) # Пример
