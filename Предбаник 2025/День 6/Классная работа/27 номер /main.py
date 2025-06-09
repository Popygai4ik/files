from turtle import *

def ris(a):
    tracer(0)
    k = 15
    penup()
    screensize(2000,2000)
    left(90)
    color = ['red', 'black', 'blue']
    for i in range(len(a)):
        for x,y in a[i]:
            setpos(x*k,y*k)
            dot(5,color[i])


def ris2(a):
    tracer(0)
    k = 15
    left(90)
    color = ['green', 'red', 'pink']
    for i in range(len(a)):
        x,y = a[i]
        setpos(x * k, y * k)
        dot(10, color[i])
