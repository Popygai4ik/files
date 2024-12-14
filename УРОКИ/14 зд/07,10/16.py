s = 654**25 + 927**13 + 243**5 - 44**2 + 2025
res  = []
dv_25 = str(int(str(s), 25))
alf = 'abcdefghijklmnopqrstuvwxyz'
for bykva in alf:
    res.append(dv_25.count(bykva))
print(res)
print(dv_25)
print(sum(res))
print(int('2126', 25))
n = 654**25 + 927**13 + 243**5 - 44**2 + 2025

cnt = 0

while n > 0:

   if n % 25 > 9:

       cnt += 1

   n //= 25

print(cnt)