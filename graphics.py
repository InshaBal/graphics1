import turtle
turtle.bgcolor("Black")
turtle.pensize(3)
turtle.speed(0)
b=["red","blue","green","purple"]
for i in range(9):
    for a in b:
        turtle.color(a)
        turtle.circle(100)
        turtle.left(20)
turtle.mainloop()