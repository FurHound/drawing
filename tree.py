import turtle
import random

BG_COLOR = 'black'
turtle.bgcolor(BG_COLOR)

t = turtle.Turtle()
def createRec(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def createTree(xcor, ycor, branchW, branchH, TreeC, times, definedspeed):
    t.speed(definedspeed)
    createRec(-50, -200, 50, 100, 'brown')
    for r in range(times):
        createRec(xcor, ycor, branchW, branchH, TreeC)
        xcor = xcor + 3
        ycor = ycor + branchH
        branchW = branchW - 6

createTree(-150, -100, 250, 6, 'green', 35, 16)


def drawStar(starX, starY, color, lengthSide):
    t.speed(9)
    t.penup()
    t.color(color)
    t.goto(starX, starY)
    t.begin_fill()
    t.pendown()
    for i in range(5):
        t.forward(lengthSide)
        t.right(144)
    t.end_fill()


drawStar(-50, 130, 'yellow', 50)

def createCircle(x, y, radius, color):
    t.penup()
    t.color(color)
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

createCircle(200, 200, 50, 'white')
createCircle(185, 200, 50, 'black')

for r in range(20):
    x = random.randint(-400, 400)
    y = random.randint(150, 400)
    lengthSide = random.randint(10, 60)
    drawStar(x, y, 'white', lengthSide)




turtle.done()