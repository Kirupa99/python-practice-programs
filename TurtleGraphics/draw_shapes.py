from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("turtle")

timmy.color("black")

#Draw Square

timmy.penup()
timmy.goto(-300,150)
timmy.pendown()
timmy.fillcolor("blue")
timmy.begin_fill()
for i in range(0,4):
    timmy.forward(50)
    timmy.left(90)
timmy.end_fill()

#Draw rectangle
timmy.penup()
timmy.goto(-200,150)
timmy.pendown()
timmy.fillcolor("green")
timmy.begin_fill()
for i in range(2):
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
timmy.end_fill()

#Draw triangle
timmy.penup()
timmy.goto(-50,150)
timmy.pendown()
timmy.fillcolor("red")
timmy.begin_fill()
for i in range(3):
    timmy.forward(100)
    timmy.left(120)
timmy.end_fill()

# Draw a circle
timmy.fillcolor("yellow")
timmy.begin_fill()
timmy.penup()
timmy.goto(120,150)
timmy.pendown()
timmy.circle(50)
timmy.end_fill()

#Draw dotted lines
timmy.color("orange")
timmy.penup()
timmy.goto(-300,100)
timmy.pendown()
for i in range(40):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

#Draw pentagon
timmy.penup()
timmy.goto(-300,0)
timmy.pendown()
timmy.fillcolor("pink")
timmy.begin_fill()

for i in range(5):
    timmy.forward(50)   # side length
    timmy.left(72)
timmy.end_fill()

my_screen=Screen()
my_screen.exitonclick()
