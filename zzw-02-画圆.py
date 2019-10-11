import turtle
turtle.penup()
turtle.showturtle()
a = ['red', 'orange', 'blue', 'green', 'gold', 'indigo']
for i in range(5, 0, -1):
    turtle.goto(0, -10*i)
    turtle.color(a[i], a[i])
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50+10*i)
    turtle.end_fill()
    turtle.penup()

turtle.hideturtle()
turtle.exitonclick()

print()
