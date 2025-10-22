import turtle

pen = turtle.Turtle()
pen.speed(0)  # fastest speed
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(60):  # number of squares
    pen.color(colors[i % 6])  # cycle through colors
    for j in range(4):  # draw one square
        pen.forward(100)
        pen.right(90)
    pen.right(6)  # small rotation for the spiral effect

turtle.done()
