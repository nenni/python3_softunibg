from .base import Figure


class RegularPolygon(Figure):

    def __init__(self, radius, num_sides, **kwargs):
        super().__init__(**kwargs)
        try:
            radius = int(radius)
            num_sides = int(num_sides)
        except ValueError as e:
            raise ValueError("Error invalid polygon input data" + str(e))

        if radius <= 0:
            raise ValueError("Error polygon radius must be > 0")
        if num_sides <=2:
            raise ValueError("Error polygon num sides must be > 2")

        self.radius = radius
        self.num_sides = num_sides

    def draw(self, turtle):
        turtle.penup()
        turtle.home()
        turtle.goto(self.center_x, self.center_y - self.radius)
        turtle.pendown()
        turtle.color(self.color)
        turtle.circle(radius=self.radius, steps=self.num_sides)
        turtle.penup()
        turtle.goto(self.center_x, self.center_y)

