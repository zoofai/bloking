import turtle as t 
import colorsys as cs

t.speed(10)
t.setup(800,800)
t.tracer(10)
t.width(2)
t.bgcolor("black")

for j in range (25):
    for i in range (15):
        t.color(cs.hsv_to_rgb(i/15, j/25,1))
        t.right(90)
        t.circle(200-j*4,90)
        t.left(90)
        t.circle(200-j*4,90)
        t.right(180)
        t.circle(50,24)
t.hideturtle()
t.done()