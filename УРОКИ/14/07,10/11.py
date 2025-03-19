from string import *
slf = '0123456789AB'
for x in slf:
    s = int(f"32D{x}", 16) + int(f"43{x}B", 12)
    if s %15==0:
        print(x, s)

for x in "0123456789AB":

    first = int(f"32D{x}", 16)

    second = int(f"43{x}B", 12)

    if ((second + first) % 15 == 0):
        print(str(second + first))
        print(str(second + first)[0])