from turtle import *
def ris(a):
    left(90)
    penup()
    tracer(0)
    k = 50
    colors = ['black','red','pink']
    for i in range(len(a)):
        for x,y in a[i]:
            goto(x*k,y*k)
            dot(3,colors[i])
def ris2(a):
    left(90)
    tracer(0)
    k = 50
    penup()
    colors = ['orange','black','gray']
    for i in range(len(a)):
        x,y = a[i][0], a[i][1]
        goto(x*k,y*k)
        dot(10,colors[i])