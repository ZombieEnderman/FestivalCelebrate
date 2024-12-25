from turtle import *

def draw_star(size):
    color('yellow')
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

def tp(x,y):
    up()
    goto(x,y)
    down()

def draw_trunk(width,high):
    color('#642100')
    begin_fill()
    for _ in range(2):
        forward(width)
        right(90)
        forward(high)
        right(90)
    end_fill()

def draw_leaf(size):
    color('#00aa00')
    begin_fill()
    for _ in range(3):
        forward(size)
        left(120)
    end_fill()

bgcolor('#000000')
tp(-15,170)
draw_star(50)
tp(-10,-50)
draw_trunk(40,100)
for z in range(1,6):
    tp(-50, -100 + z * 30)
    draw_leaf(120)
color('#000000')
done()