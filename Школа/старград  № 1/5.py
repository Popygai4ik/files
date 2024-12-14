def f(n):
    b_nn = bin(n)[2:]
    if n % 2 == 0:
        b_nn = '11'+b_nn
    else:
        b_nn = '1'+b_nn+'10'
    r= int(b_nn, 2)
    return r
# for i in range(123_456_789,456789013):
#     print(f'i = {i} r = {f(i)}')
print(f(456789011))