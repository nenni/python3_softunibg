#!/usr/bin/env python3

"""
Lecture 2 - Exercise 3
Ще направим инициали на имена. Лесно звучи, нали?
По въведени имена с input() искаме програмата да покаже как това име ще се съкрати до инициали.
Пример как трябва да изглежда програмата:
Въведете име:  Борис Червенков
Инициали: Б.Ч.

Правилата:
* От всяка част от името трябва да остане по една буква,
след което да има точка;
например ако въведем 3 или повече имена - Име Презиме Фамилия,
програмата трябва да покаже И.П.Ф.;
*Програмата трябва да може да работи на кирилица и на латиницa -
John Lawrence Smith -> J.L.S.;

Date: 20160112
version: 0.1
"""


user_name = input("Въведете име: ")

# print(user_name)
user_list = user_name.split()
# print(user_list)

initials = ''
exit_flag = True

for i, w in enumerate(user_list):
    if w.isalpha():
        initials += w[0] + "."
    else:
        print("Грешка! Името трябва да съдържа само букви")
        exit_flag = False
        break

if exit_flag:
    print("Инициали: " + initials)
