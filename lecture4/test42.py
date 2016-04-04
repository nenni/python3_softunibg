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
"""
import logging


def read_file_return_ave_sum(file):
    total = 0
    count = 0
    try:
        with open(file) as f:
            # print(list_lines)
            for line_number, line in enumerate(f):
                # print(line)
                values = line.rsplit(',')
                # print(values)
                if values and values[0] and len(values) == 7:
                    total += float(values[-1])
                    count += 1
                else:
                    logging.warning("Invalid line {} in {}".format(line_number+1, file))

        # print(count)
        if count > 0:
            print("{:.2f}, {}".format(total, count))
            return total/count
        else:
            print("File {} is empty".format(file))
            return 0


    except FileNotFoundError as e:
        print("File {} does not exist".format(file))
        return 0




# read_file_return_ave_sum("catalog_sample.csv")

# FILENAME1 = "catalog_sample.csv"
# print("{} - average price: "
#       "{average_price:.2f}".format(FILENAME1, average_price=read_file_return_ave_sum(FILENAME1)))
#
# print("-"*30)

FILENAME2 = "catalog_full.csv"
print("{} - average price: "
      "{average_price:.2f}".format(FILENAME2, average_price=read_file_return_ave_sum(FILENAME2)))
#
# print("-"*30)
#
# FILENAME0 = "test.txt"
# print("{} - average price: "
#       "{average_price:.2f}".format(FILENAME0, average_price=read_file_return_ave_sum(FILENAME0)))
#
# print("-"*30)
#
# FILENAME_EMPTY = "empty.txt"
# print("{} - average price: "
#       "{average_price:.2f}".format(FILENAME_EMPTY, average_price=read_file_return_ave_sum(FILENAME_EMPTY)))