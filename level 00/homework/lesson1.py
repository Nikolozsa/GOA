

import turtle


screen = turtle.Screen()
screen.title("Simple House Drawing")


house = turtle.Turtle()
house.speed(1)


house.penup()
house.goto(-50, -50)
house.pendown()
house.begin_fill()
house.color("blue")
house.forward(100)
house.left(90)
house.forward(100)
house.left(90)
house.forward(100)
house.left(90)
house.forward(100)
house.left(90)
house.end_fill()

house.penup()
house.goto(-50, 50)
house.pendown()
house.begin_fill()
house.color("red")
house.setheading(0)
house.forward(100)
house.left(135)
house.forward(70)
house.left(90)
house.forward(70)
house.left(135)
house.forward(100)
house.end_fill()


house.penup()
house.goto(-15, -50)
house.pendown()
house.begin_fill()
house.color("brown")
house.setheading(90)
house.forward(40)
house.right(90)
house.forward(30)
house.right(90)
house.forward(40)
house.end_fill()


house.penup()
house.goto(-45, -20)
house.pendown()
house.begin_fill()
house.color("white")
house.setheading(0)
house.forward(20)
house.left(90)
house.forward(20)
house.left(90)
house.forward(20)
house.left(90)
house.forward(20)
house.end_fill()


house.penup()
house.goto(25, -20)
house.pendown()
house.begin_fill()
house.color("blue")
house.setheading(0)
house.forward(20)
house.left(90)
house.forward(20)
house.left(90)
house.forward(20)
house.left(90)
house.forward(20)
house.end_fill()


house.hideturtle()
turtle.done()