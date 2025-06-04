# k = 2048*512
# I = 2 * 1024*1024*8
# print(2 ** (I/k))
# k = 1024*1024
# I = 1 * 2 ** 23
# print(I/k)
# k = 512*256
# i = 9
# print((k*i)/(2 ** 13))
# k = 2560*1440
# i = 16
# for n in range(1,10000):
#     if (k * i * n)/2**33<= 8:
#         print(n)
# n = 1165
# print(3135 - 1165- 1165)
# k = 4890*3570
# i = 22
# k2 = 1360*1240
# i2 = 7
# print((((i*k)-(i2*k2))*200)/2**13)
# k = 2
# v = 32000
# i = 32
# I = 16*2**23
# for t in range(1,1000):
#     if t*v*i*k == I:
#         print(t)
# k = 192 * 960
# I = (100*75/85)*2**13
# print(I/k)
# i=4
# print((((i*k) / 2**13)*0.75))
# k = 768*512
# I = 640*2**13
# print(I/k)
# print(13*k/2**13)
# i = 13-5
# print(2**i)
# k = 64*1536
# I = 252*2**13
# print(I/k)
# print(21/3)# 2+1+2+1
# print((32000*16*4*60)/2400)
# v= 131072
# k = 2048*1536
# i=6*8
# print((k*i)/v)
# k=1920*1920
# # print(2**14)
# i = 14
# v = 1_474_560
# for n in range(1,1000):
#     if (n*k*i)/v <= 280:
#         print(n)
import math

# k = 20
# a = 11*2+10
# # print(a)
# i = (math.log2(a))
# print((13*60))

# k = 400
# a = 10+4090
# i = math.ceil(math.log2(a))
# I1 = math.ceil(k*i/8)
# # print(I1)
# print(I1*16384/2**10)

# k = 23
# a = 65*2+10
# i = math.ceil(math.log2(a))
# I1 = math.ceil(i*k/8)+49
# print(I1)
# for n in range(1,100):
#     if (n*I1) <= 4 * 1024:
#         print(n)
# k = 17
# a = 26*2 + 10+6
# # print(a)
# i = 7
# I1 = math.ceil((k*i)/8)
# # print(2**12)
# p1 = (2)
# print(70-p1-I1)
# a = 10+52+4044
# i = math.ceil(math.log2(a))
# for k in range(1,1000):
#     I1 = math.ceil(k*i/8)
#     if (7777*I1/2**10)<= 566:
#         print(k)
# k = 256
# for n in range(1,1000):
#     i = math.ceil(math.log2(n))
#     I1 = math.ceil(k * i / 8)
#     if (32768 * I1)/2**20 >8:
#         print(n)
# a = 10+52+980
# i = math.ceil(math.log2(a))
# for k in range(1,1000):
#     I1 = math.ceil(i*k/8)
#     if (385*I1/2**10)<=136:
#         print(k)
k = 840*110
i = math.ceil(math.log2(2543))
# print(i)
I1 = i*k*0.5
n = 624
# for n in range(1,1000):
#     if (n * I1)/(1_459_960) <= 237:
#         print(n)
print((237*1_459_960 - I1*n)/8)