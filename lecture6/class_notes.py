
class Figure:

    def __init__(self, center, color):
        self.position = center
        self.color = color

    def __str__(self):  # toString() or ToString() in other languages
        return "Figure center: {}, color: {}".format(self.position, self.color)

    def print_figure(self):
        print("Figure position is {} and color is {}".format(
            str(self.position).upper(), self.color
        ))


class Circle(Figure):

    def __init__(self, center, color, radius):
        super(Circle, self).__init__(center, color)
        self.radius = radius

    def __str__(self):  # toString() or ToString() in other languages
        return \
            super().__str__() + ", radius: {}".format(self.radius)

    def print_figure(self):
        """
        when overwriting method of the parent class keep method with the same parameters
        Figure print_figure(self) and child Circle method print_figure(self)
        :return:
        """
        print("Circle position is {} and color is {} and radius is {}".format(
            self.position, self.color, self.radius
        ))


f = Figure('left', 'red')
f.print_figure()
f.position = 'right'
f.print_figure()


c = Circle('center', 'black', 20)
c.print_figure()

print(f)
print(c)
# print(isinstance(c, Figure))
# print(isinstance(c, Circle))
# print(isinstance(f, Figure))
# print(isinstance(f, Circle))
#
# print(issubclass(Circle, Figure))
# print(issubclass(Figure, Circle))



