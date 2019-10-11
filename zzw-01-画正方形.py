# coding=utf-8
import turtle

def squartage(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

size = 100
a = ['red', 'green', 'brown', 'blue', 'orange']
turtle.showturtle()
for j in range(5):
    turtle.begin_fill()
    turtle.color(a[j], a[j])
#    turtle.fillcolor(a[j])
#    turtle.pencolor(a[j])
    squartage(size)
    turtle.end_fill()
    size +=20

turtle.hideturtle()
turtle.write("画正方形", font = ("Times", 18, "bold"))
turtle.exitonclick()
