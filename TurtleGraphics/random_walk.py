import random
from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("turtle")
timmy.pensize(10)
colours=["red","green","yellow","blue","orange","black","cyan","purple","brown"]
movement=["forward","left","right"]
x=0
my_screen=Screen()
my_screen.setup(width=600, height=600)
boundary=280

timmy.speed(5)
def random_walk(colours,movement,boundary):
    for i in range(200):
        timmy.color(random.choice(colours))
        move=random.choice(movement)
        if move == "forward":
            timmy.forward(50)
        elif move == "left":
            timmy.left(90)
        elif move == "right":
            timmy.right(90)
        x,y=timmy.xcor(),timmy.ycor()
        if abs(x)>boundary or abs(y)>boundary:
            timmy.right(180)

random_walk(colours,movement,boundary)


