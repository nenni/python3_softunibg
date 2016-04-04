

def print_temperature(temp):
    print(temp, 'C')

print_temperature(45)


def convert_faren_to_cel(deg_f):
    return (deg_f - 32) / 1.8
    # pass

print_temperature(convert_faren_to_cel(45))


# multiple arguments
def test_fun(a, b, c):
    print(a, b, c)


test_fun(1, 2, 3)

# TODO naming arguments:


# default value of the argument if not passed to the function
def print_temperature(temp, dec_digits=2):
        print('Температура е: {:.{limit_digit}f} C'.format(temp, limit_digit=dec_digits))

print_temperature(2, 3)
print_temperature(convert_faren_to_cel(50))
print_temperature(convert_faren_to_cel(50), 5)
print_temperature(convert_faren_to_cel(50), dec_digits=7)


########
# Променлив брой аргументи *args и **kwargs
########
# *args e tuple
def sum_numbers(*args):
    total = 0
    for n in args:
        total += n
    return total

print('Sum is: ', sum_numbers(1, 67, 89, 14, 90, 15, 16, 17, 14, 16, 56, 89))


# във функцията **kwargs ще бъде обикновен dict
def pretty_print_record(**kwargs):
    print("Record:")
    for k, v in kwargs.items():
        print("\t", k, "= ", v)

pretty_print_record(name="Mercury", distance_au=0.387, diameter_km=4878)
pretty_print_record(name="Venus", distance_au=0.723, diameter_km=12104)
pretty_print_record(name="Earth",
                    distance_au=1,
                    diameter_km=12742,
                    average_temp_c=7.2,
                    atmosphere=["nitrogen", "oxygen", "argon"])
pretty_print_record()


# def pretty_print_record(**kwargs):   # във функцията kwargs ще бъде обикновен dict
#     print(kwargs.pop('name', "Record"), ":")
#     for k, v in kwargs.items():
#         print("\t", k, "= ", v)
#
# pretty_print_record(name="Venus", distance_au=0.723, diameter_km=12104)
# pretty_print_record(distance_au=0.723, diameter_km=12104)

