import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed('fastest')
x = 10

for y in range(12):
    t.color('green')
    t.forward(5 * x)
    x += 1
    # t.left(13)
    for i in range(10):
        t.color('red')
        t.left(138)
        t.forward(20)

turtle.exitonclick()
