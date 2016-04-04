#!/usr/bin/env python3 -tt

"""
Да си направим програмка за запознанства.

В едно list-че сме си съчинили малко информация за момиченца и момченца.
От данните, програмата трябва да изведе резултати кои хора биха си паснали, съгласно следните правила:

*момиченце с момченце; ако сте по-свободомислещи,
можете да комбинирате и момченце с момченце, но все пак да има някакво правило :о);
*трябва да имат поне един общ интерес;

Примерен резултат:
Мария и Георги - общ интерес: плуване
"""

people = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'gender': "female",
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'gender': "female",
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'gender': "female",
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'gender': "female",
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'gender': "female",
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'gender': "male",
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'gender': "male",
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'gender': "male",
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'gender': "male",
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'gender': "male",
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'gender': "male",
    },
    {
        'name': "Калоян",
        'interests': ['история', 'покер', 'пътуване', 'автомобили'],
        'gender': "male",
    },
]


female_list = []
male_list = []

for i in people:
    if i['gender'] == 'female':
        female_list.append(i)
    elif i['gender'] == 'male':
        male_list.append(i)
    else:
        print('Gender not specified for:', i['name'])


if female_list and male_list:
    for f in female_list:
        print("---------------------------------------------------------")
        for m in male_list:
            common_f_m = set(f['interests']).intersection(set(m['interests']))
            if common_f_m:
                print(f['name'], 'и', m['name'], '- общ интерес: ', end='')
                a = ''
                for idx, value in enumerate(common_f_m):
                    if idx == len(common_f_m) - 1:
                        a += value
                    else:
                        a += value + ', '
                print(a)
    print("---------------------------------------------------------")

