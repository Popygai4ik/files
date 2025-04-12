from turtle import *
def ris(a):
    tracer(0)
    screensize(2000,2000)
    penup()
    left(90)
    k = 50
    colors = ['red','black','pink','orange', 'gray']
    for i in range(len(a)):
        for x,y in a[i]:
            goto(x*k,y*k)
            dot(5,colors[i])

def ris2(a):
    tracer(0)
    screensize(2000,2000)
    penup()
    left(90)
    k = 50
    colors = ['pink','orange', 'black','gray','purple']
    for i in range(len(a)):
        x,y = a[i]
        goto(x * k, y * k)
        dot(10, colors[i])