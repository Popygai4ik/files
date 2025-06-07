f = open('24_1_дз.txt')
s = f.readline()
for i in range(1,100):
    if 'B'*i in s:
        print(i,"B" * i )