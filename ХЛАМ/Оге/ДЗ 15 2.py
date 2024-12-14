num = int(input())
mack = 0
r = 'No'
for i in range(num):
    c = int(input())
    if c > mack:
        mack = c
    if c < 30:
        r = 'Yes'
print(f'Макс скорость {mack} и скорость авто была меньше 30: {r}')
4
29
69
63
66