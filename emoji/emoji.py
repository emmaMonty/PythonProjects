import turtle

#circle
turtle.begin_fill()
turtle.color("yellow")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(100)
turtle.end_fill()

#eye 1
turtle.begin_fill()
turtle.color("black")
turtle.penup()
turtle.goto(25, 125)
turtle.pendown()
turtle.circle(10)
turtle.end_fill()

#eye 2
turtle.begin_fill()
turtle.color("black")
turtle.penup()
turtle.goto(-25, 125)
turtle.pendown()
turtle.circle(10)
turtle.end_fill()

#face mask
turtle.begin_fill()
turtle.color("red")
turtle.penup()
turtle.goto(0,-120)
turtle.pendown()
turtle.circle(145, steps = 3)
turtle.end_fill()

#hat
turtle.color("black")
turtle.pensize(50)
turtle.penup()
turtle.goto(-10,185)
turtle.pendown()
turtle.forward(125)
turtle.right(-90)
turtle.forward(25)
turtle.right(-90)
turtle.forward(75)
turtle.right(90)
turtle.forward(100)
turtle.right(-90)
turtle.forward(75)
turtle.right(90)
turtle.forward(-100)
turtle.right(-90)
turtle.forward(75)
turtle.right(-90)
turtle.forward(25)
turtle.right(-90)
turtle.forward(125)

#font
turtle.penup()
turtle.goto(-10, -200)
turtle.pendown()
turtle.write("Howdy Y'all ", font = ("Times", 20, "bold"))
turtle.hideturtle()

turtle.done()
