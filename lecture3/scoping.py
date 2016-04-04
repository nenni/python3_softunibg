

counter = 1


def do_some_work(counter):
    counter += 10
    #  променливата counter във функцията няма нищо общо с променливата counter извън функцията.

do_some_work(counter)
print(counter)
# резултатът ще е 1

#######
# variable counter is not accessible from the function
# counter = 1
#
# def do_some_work():
#     counter += 10
#
# do_some_work()
#  ще получим UnboundLocalError: local variable 'counter' referenced before assignment грешка,
# понеже Python не знае какво е counter в контекста на функцията.


"""
Важно - Използването на global в който и да е език за програмиране е много ясен индикатор,
че нещо не е наред с архитектурата и логиката на Вашия код.
Опитвайте се да пишете кода така, че да не Ви се налага да използвате global.
Разбира се, понякога е неизбежно, но се постарайте в рамките на разумното да не го използвате.
"""
counter = 1


def do_some_work():
    global counter
    counter += 10

do_some_work()
print(counter)
# резултатът ще е 11 понеже Python може да намери променливата counter извън тялото на функцията.

#
# num0 = 0
# num1 = 5
# num2 = 4
#
#
# def sum2():
#     num0 += num1 + num2
#     return num0
#     # return num1 + num2
#
# # print(sum2())
# print(sum2())
# print(num0)



import copy


def l_append(list1):
    new_l = copy.copy(list1)
    new_l.append(345)
    return new_l

list1 = [1, 2, 3, 4]


print("copy list in function l_append(), returns: ", end='')
print(l_append(list1))
print("original list: ", end='')
print(list1)



