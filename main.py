import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
leonardo.speed(1)
michelangelo.speed(1)
x = random.randrange(1,100)
leonardo.forward(x)
michelangelo.forward(x)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

distance = random.randrange(0,10)
for move in range(10):
  leonardo.forward(distance)
  michelangelo.forward(distance)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
leonardo.speed(3)
leonardo.down()
for sides in [3, 4, 6, 9, 12]:
  for shape in range(sides):
    leonardo.forward(50)
    leonardo.left(360/sides)
  leonardo.clear()

window.exitonclick()
