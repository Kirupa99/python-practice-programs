from turtle import Turtle,Screen
timmy=Turtle()
gap=10
timmy.speed(20)
#while (timmy.xcor() == 0 and timmy.ycor() ==0):
for _ in range(int(360/gap)):
    timmy.circle(50)
    timmy.setheading(timmy.heading() + gap)

