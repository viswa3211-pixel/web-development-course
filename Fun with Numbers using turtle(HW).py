import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("lightblue")   # Background color

# Create turtle
pen = turtle.Turtle()
pen.speed(3)

# -------- Equilateral Triangle --------
pen.penup()
pen.goto(-250, 0)
pen.pendown()
pen.color("black", "red")
pen.begin_fill()

for i in range(3):
    pen.forward(100)
    pen.left(120)

pen.end_fill()

# -------- Rectangle --------
pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.color("black", "orange")
pen.begin_fill()

for i in range(2):
    pen.forward(120)
    pen.left(90)
    pen.forward(60)
    pen.left(90)

pen.end_fill()

# -------- Hexagon --------
pen.penup()
pen.goto(100, 0)
pen.pendown()
pen.color("black", "yellow")
pen.begin_fill()

for i in range(6):
    pen.forward(70)
    pen.left(60)

pen.end_fill()

# -------- Rectangle --------
pen.penup()
pen.goto(-50, -150)
pen.pendown()
pen.color("black", "blue")
pen.begin_fill()

for i in range(2):
    pen.forward(140)
    pen.left(90)
    pen.forward(70)
    pen.left(90)

pen.end_fill()

# -------- Triangle --------
pen.penup()
pen.goto(150, -150)
pen.pendown()
pen.color("black", "purple")
pen.begin_fill()

for i in range(3):
    pen.forward(100)
    pen.left(120)

pen.end_fill()

turtle.done()

