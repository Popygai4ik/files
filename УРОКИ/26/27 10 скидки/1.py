f= open('1.txt')
N = int(f.readline())
discounts = []
summ = 0
max_value = 0
for i in range(N):
  x = int(f.readline())
  if x <= 120:
      summ += x
  else:
      discounts.append(x)
discounts.sort()
for i in range(len(discounts)):
  if i < (len(discounts) // 2):
      summ += (discounts[i] * 0.75)
      max_value = discounts[i]
  else:
      summ += discounts[i]
print(int(summ)+1, max_value)