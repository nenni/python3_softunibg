#!/usr/bin/env python3 -tt

"""
Да разширим предходната задача.
Вече имаме малко повече информация за хората, и искаме да прибавим допълнителни условия към matchmaking-a.

Освен условията досега:
*момиченце с момченце; ако сте по-свободомислещи,
можете да комбинирате и момченце с момченце, но все пак да има някакво правило :о);
*трябва да имат поне един общ интерес;

ще имаме и допълнителни условия:
*разликата в годините не трябва да бъде по-голяма от 6;
*не бива да комбинирате хора с бившите им партньори - някакси ще се получи неловко :о)

Резултатът от програмата също ще трябва да заизглежда малко по-добре:
Мария (24) и Калоян (29) ; общи интереси: пътуване, кино
"""

people = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'age': 24,
        'gender': "female",
        "ex": ["Кирил", "Петър"],
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'age': 21,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'age': 34,
        'gender': "female",
        "ex": ["Борис"],
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'age': 36,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'age': 18,
        'gender': "female",
        "ex": ['Димитър'],
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'age': 27,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'age': 20,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'age': 19,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'age': 32,
        'gender': "male",
        'ex': [],
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'age': 26,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'age': 34,
        'gender': "male",
        'ex': ['Дарина'],
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'age': 22,
        'gender': "male",
        'ex': ['Галя'],
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'age': 23,
        'gender': "male",
        'ex': ["Мария"],
    },
    {
        'name': "Калоян",
        'interests': ['кино', 'покер', 'пътуване', 'автомобили'],
        'age': 29,
        'gender': "male",
        'ex': [],
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
            # Age diff logic
            age_diff = False
            if (int(f['age']) >= int(m['age'])) and int(f['age']) - int(m['age']) <= 6:
                age_diff = True
            elif (int(m['age']) >= int(f['age'])) and int(m['age']) - int(f['age']) <= 6:
                age_diff = True

            # Ex partner logic
            # print(f['ex'].__class__) = list
            # print(m['name'].__class__) = string
            # string not in list
            if m['name'] not in f['ex']:
                # Common interests logic
                common_f_m = set(f['interests']).intersection(set(m['interests']))
                if common_f_m and age_diff:
                    # print(f['name'], '(', f['age'], ') и', m['name'], '(', m['age'], ') - общ интерес: ', end='')
                    # New fancy printing
                    # print('{0} ({1}) и {2} ({3}) - общи интереси: '.format(f['name'], f['age'],
                    #                                                    m['name'], m['age']), end='')
                    # a = ''
                    # for idx, value in enumerate(common_f_m):
                    #     if idx == len(common_f_m) - 1:
                    #         a += value
                    #     else:
                    #         a += value + ', '
                    # print(a)

                    print('{0} ({1}) и {2} ({3}) - общи интереси: {4}'.format(f['name'], f['age'],
                                                   m['name'], m['age'], ', '.join(common_f_m)))
                    # break
    print("---------------------------------------------------------")


