def per(n):
    alf = '0123456789ABCDEFG'
    res = ''
    while n > 0:
        res += str(alf[n % 17])
        n = n // 17
    return res[::-1]
for n in range(4, 1000):
    w = per(n)
    w = w.replace('5','F')

'''
global dict_17

dict_17 = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F', '16': 'G'}

def seventeen(x):

   s = ""

   while x > 0:

       s += str(x % 17) + ' '

       x = x // 17

   for c in [str(i) for i in range(10, 17)]:

       s = s.replace(c, dict_17[c])

   s = ''.join(s.split(' '))

   return s[::-1]

def num_sum(x):

   s = 0

   for i in x:

       s += int(i, 17)

   return s

def alg(x):

   y = seventeen(x)

   y = y.replace('5', 'F')

   if num_sum(y) % 2 == 0:

       y += '11'

   else:

       y = '42' + y

   return int(y[::-1], 17)

for i in range(4, 100000):

   if alg(i) % 7 == 0 and alg(i) > 290:

       print(i)

       break'''