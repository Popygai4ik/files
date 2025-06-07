# s = '3'*62
# print(s)
# while '3333' in s or '777' in s:
#     if '3333' in s:
#         s = s.replace('3333','7',1)
#     else:
#         s = s.replace('777', '3', 1)
#     print(s)
# print(s)
# s = '>' + '1'*55+27*'2'+30*'3'
# while '>1' in s or '>2' in s or ">3" in s:
#     if '>1' in s:
#         s= s.replace('>1','22>3', 1)
#     if '>2' in s:
#         s = s.replace('>2', '2>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '11>2', 1)
#
# print(sum(int(i) for i in s[:-1]))

# res= []
# for n in range(4,10000):
#     s = '7'+'2'*n
#     while '72' in s or '322' in s or '2222' in s:
#         if '72' in s:
#             s = s.replace('72', '2', 1)
#         if '322' in s:
#             s = s.replace('322', '27', 1)
#         if '222' in s:
#             s = s.replace('222', '3', 1)
#     print(s,n)
#     res.append([sum(map(int,s))])
# print(max(res))
from  turtle import *

# tracer(0)
# left(90)
# pendown()
# k = 20
# for i in range(4):
#     forward(10*k)
#     right(270)
# penup()
# forward(3*k)
# right(270)
# forward(5*k)
# right(90)
# pendown()
# for i in range(2):
#     forward(10*k)
#     right(270)
#     forward(12*k)
#     right(270)
# penup()
# for x in range(-30, 30):
#     for y in range(-30,30):
#         goto(x*k,y*k)
#         dot()
# done()
# tracer(0)
# left(90)
# pendown()
# k=10
# screensize(2000,2000)
# for i in range(2):
#     forward(24*k)
#     right(90)
#     forward(20*k)
#     right(90)
# penup()
# forward(7*k)
# right(90)
# forward(7*k)
# left(90)
# pendown()
# for i in range(2):
#     forward(60*k)
#     right(90)
#     forward(100*k)
#     right(90)
# penup()
# for x in range(-30,30):
#     for y in range(-30, 30):
#         setpos(x*k,y*k)
#         dot()
# # done()
# tracer(0)
# left(90)
# pendown()
# k=10
# screensize(2000,2000)
# for i in range(4):
#     forward(16*k)
#     right(90)
#     forward(22*k)
#     right(90)
# penup()
# forward(5*k)
# right(90)
# forward(5*k)
# left(90)
# pendown()
# for i in range(16):
#     forward(52*k)
#     right(90)
#     forward(77*k)
#     right(90)
# penup()
# for x in range(-30,30):
#     for y in range(-30, 30):
#         setpos(x*k,y*k)
#         dot()
# done()
# res = []
# for n in range(4,10000):
#     s = '2'+n*'9'
#     while '29' in s or '399' in s or '99' in s:
#         if '29' in s:
#             s = s.replace('29','9', 1)
#         if '399' in s:
#             s = s.replace('399','92',1)
#         if '99' in s:
#             s = s.replace('99', '3', 1)
#     c_n = 0
#     for i in '13579':
#         c_n += s.count(i)
#     if c_n == 10:
#         print(n)
tracer(0)
left(90)
k = 20
for i in range(3):
    forward(12*k)
    right(120)
penup()
right(60)
forward(6*k)
left(60)
pendown()
for i in range(3):
    forward(15*k)
    right(90)
    forward(24*k)
    right(90)
penup()
screensize(2000,2000)
for x in range(-30,30):

    for y in range(-30, 30):
        setpos(x*k,y*k)
        dot()
done()