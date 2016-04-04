#!/usr/bin/env python3 -tt

"""
Свалете тези два файла (catalog_sample.csv) и (catalog_full.csv)
Файловете са реален продуктов каталог на на известен производител на спортни стоки,
с описание и цени (цените са произволни), като разликата между двата файла е в броя на артикулите.
catalog_sample има само 200 артикула,
докато
catalog_full има над 60000.
Структурата на двата файла е еднаква.

catalog_sample.csv
catalog_full.csv

Напишете програма, която намира средната цена от всички артикули във файла.

Структурата на CSV файловете е следната:

каталожен номер
име на продукта
цветове на продукта. Ако са повече от един са разделени с /
за какъв вид активност е предназначен артикула
каква е групата на артикула
за кой пол и възраст е предназначен артикула
цена
Разделителят на данните е , (запетая), а десетичният знак е . (точка)



Използвайки кода си от предишната задача, и използвайки същите файлове,
намерете средната цена от всички продукти в каталога, групирани по пол и възраст.
Използвайте колоната за пол и възраст която има една от следните стойности:
infant
kid
men
unisex
woman
"""
import logging


# files = ["catalog_sample.csv", "catalog_full.csv", "empty.txt"]
files = ["catalog_sample.csv"]

for file in files:

    total_infant = 0
    total_kid = 0
    total_men = 0
    total_woman = 0
    total_unisex = 0

    list_infant = []
    list_kid = []
    list_men = []
    list_woman = []
    list_unisex = []

    try:
        with open(file) as input_file:
            for line_number, line in enumerate(input_file):
                # print(line)
                values = line.rsplit(',', 2)
                # print(values)

                if values and values[0] and len(values) == 3:
                    age_type = values[-2]
                    item_price = float(values[-1])

                    if age_type == 'Infant':
                        list_infant.append(age_type)
                        total_infant += item_price
                    elif age_type == 'Kid':
                        list_kid.append(age_type)
                        total_kid += item_price
                    elif age_type == 'Men':
                        list_men.append(age_type)
                        total_men += item_price
                    elif age_type == 'Woman':
                        list_woman.append(age_type)
                        total_woman += item_price
                    elif age_type == 'Unisex':
                        list_unisex.append(age_type)
                        total_unisex += item_price
                    else:
                        print("{} is not recognize age type".format(age_type))
                else:
                    logging.warning("Invalid line {} in {}".format(line_number+1, input_file))

            #
            # print age type and average price
            #

            if len(list_infant) > 0:
                print("{} - {}, average price is: {:.2f}".format(file, "Infant", total_infant/len(list_infant)))
            else:
                print("{} is empty".format(file))

            if len(list_kid) > 0:
                print("{} - {}, average price is: {:.2f}".format(file, "Kid", total_kid/len(list_kid)))
            else:
                print("{} is empty".format(file))

            if len(list_men) > 0:
                print("{} - {}, average price is: {:.2f}".format(file, "Men", total_men/len(list_men)))
            else:
                print("{} is empty".format(file))

            if len(list_woman) > 0:
                print("{} - {}, average price is: {:.2f}".format(file, "Woman", total_woman/len(list_woman)))
            else:
                print("{} is empty".format(file))

            if len(list_unisex) > 0:
                print("{} - {}, average price is: {:.2f}".format(file, "Unisex", total_unisex/len(list_unisex)))
            else:
                print("{} is empty".format(file))

            print("-"*30)
    except FileNotFoundError as e:
        print("File {} does not exist".format(file))

