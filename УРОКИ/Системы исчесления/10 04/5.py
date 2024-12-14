from string import *
ascii_uppercase = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def to_9(s):
    x9 =''
    while s > 0:
        x9 += str(ascii_uppercase[s % 9])
        s = s // 9
    return x9[::-1]
for x in ascii_uppercase[:30]:
    for y in ascii_uppercase[:20]:
        mn1 = (x+'11'+x+'2'+x+'3'+x+'4')
        mn2 = ('11'+y+'2'+y+'3'+y+'4'+y)
        res = int(str(mn1), 30) - int(str(mn1), 20)
        print(res)
from string import *

alph = digits + ascii_uppercase[:20]

mx = 0

for i in range (30):

    for j in range (20):

        x = alph[i]

        y = alph[j]

        value_first = int(x + "11" + x + "2" + x + "3" + x + "4", 30)

        value_second = int("11" + y + "2" + y + "3" + y + "4" + y, 20)

        value = value_first - value_second

        sum_dig = 0

        while value > 0:

            sum_dig += value % 9

            value //= 9

        mx = max(mx, sum_dig)

print(mx)