import turtle

side = 40
t = turtle.Turtle()
t.speed('fastest')
pos_x = -160
pos_y = -100

t.penup()
t.goto(pos_x, pos_y)
t.pendown()
"""
loop for rows
"""
for y in range(8):

    """
    loop for columns
    """
    for i in range(8):
        """
        logic for filling odd or even cells
        """
        if y % 2 == 0:
            if i % 2 == 0:
                t.begin_fill()
        else:
            if i % 2 != 0:
                t.begin_fill()
        """
        draw rectangle 4 sides
        """
        for x in range(4):
            t.forward(side)
            t.left(90)
        """
        end of the filling and move forward
        """
        t.end_fill()
        t.forward(side)
    """
    move the pen one row up
    """
    t.penup()
    pos_y += 40
    t.goto(pos_x, pos_y)
    t.pendown()

turtle.exitonclick()
