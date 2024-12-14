from itertools import *

# c = 0
# for i in permutations('ДИАНА', 5):
#     if len(set(i)) == 5:
#         c += 1
# print(c)
from itertools import *

cnt = 0

for i in set(permutations("ДИАНА", 5)):

    if "АА" not in "".join(i):

        cnt += 1

print(cnt)