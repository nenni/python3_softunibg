import turtle

wn = turtle.Screen()

side_len = input('Enter the side length: ')

for i in range(4):
    turtle.forward(int(side_len))
    turtle.left(90)

wn.mainloop()
