
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


def read_file_return_ave_sum(file):
    sum_ave = 0
    num_lines = 0

    with open(file) as f:
        list_lines = f.readlines()
        # print(list_lines)
        for line in list_lines:
            line_list = (line.rstrip()).split(',')
            # print(line_list[-1])
            sum_ave += float(line_list[-1])
            num_lines += 1
    print(sum_ave, num_lines)
    average_price = sum_ave/num_lines
    return average_price


print("Sample file Average price: "
      "{average_price:.2f}".format(average_price=read_file_return_ave_sum("catalog_sample.csv")))

print("-"*30)
print("Full file Average price: "
      "{average_price:.2f}".format(average_price=read_file_return_ave_sum("catalog_full.csv")))




