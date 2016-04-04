import turtle

g = 134
l = 120

no_iter = input('Въведи брой итерации: ')
x = 0
while x < int(no_iter):
    turtle.left(g)
    turtle.forward(l)
    x += 1
