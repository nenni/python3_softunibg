
def something(a):
    if a % 2 == 0:
        return a**2
    else:
        a -= 1
        return a

for i in range(10):
    print(something(i))





