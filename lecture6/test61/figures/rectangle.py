from .base import Figure


class Rectangle(Figure):

    def __init__(self, center_x, center_y, color, width, height, **kwargs):
        super().__init__(center_x, center_y, color, **kwargs)
        self.width = width
        self.height = height

    def draw(self, turtle):
        half_width_side = self.width / 2
        half_height_side = self.height / 2
        left = self.center_x - half_width_side
        top = self.center_y - half_height_side

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        for i in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)

        turtle.penup()
        turtle.goto(self.center_x, self.center_y)

