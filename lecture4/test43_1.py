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


# files = ["catalog_sample.csv", "catalog_full.csv", "empty.txt", "nofile.txt"]
files = ["catalog_sample.csv"]

for file in files:

    age_type_price_dict = {}

    try:
        with open(file) as input_file:

            input_file.seek(0)
            if not input_file.read(1):
                # logging.warning("File {} is empty".format(file))
                raise ValueError("File {} is empty".format(file))

            else:
                input_file.seek(0)

                for line_number, line in enumerate(input_file):

                    values = line.rsplit(',', 2)

                    if values and values[0] and len(values) == 3:
                        age_type = values[-2]
                        item_price = values[-1].rstrip()

                        if age_type not in age_type_price_dict:
                            age_type_price_dict[age_type] = [float(item_price)]
                        else:
                            age_type_price_dict[age_type].append(float(item_price))

                    else:
                        logging.warning("Invalid line {} in {}".format(line_number+1, input_file))

                #
                # print age type and average price
                #
                for key, value in age_type_price_dict.items():
                    total = sum(value)
                    average_price = total/len(value)
                    # print(key, value)

                    if len(value) > 0:
                        print("File name {filename} - category {key} average price is: {ave_price:.2f}".format(
                            key=key,
                            ave_price=average_price,
                            filename=file
                        ))
                    else:
                        print("No prices found for {}".format(key))

    except FileNotFoundError as e:
        print("Exception: {}".format(e))
    except ValueError as e:
        print("Exception: {}".format(e))

    print("-"*70)

