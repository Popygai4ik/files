def prost(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


c = 0
for n in range( 610_001, 610_100 +1000):
    for i in range(2, n):
        if n % i == 0:
            if prost(n//i):
                c += 1
                print(n, n // i)
            break
    if c == 6:
        break