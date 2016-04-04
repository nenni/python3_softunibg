#!?usr/bin/env python3 -t
"""
Вие сте собственик на online магазин, и искате да проверите в кои дни и часове има най-много продажби.
Най-много продажби означава сумата на тези продажби, не броят на извършените продажби.

Свалете файла, който съдържа 1000 продажби.
Файлът е CSV като първата колона е датата и часа на продажбата,
втората колона е сумата на продажбата. Файлът не е подреден.

Напишете код, който показва в кой ден е имало най-много продажби като сума от всички продажби за този ден.

Пример:
В понеделник е имало продажби за 2000 лева,
във вторник за 2345 лева, а в сряда за 897 лева.
Денят с най-много продажби е вторник.
"""

import sys
import logging
from datetime import datetime
import csv


def date_hour_sales_entry(row_list):

    try:
        if len(row_list) == 2:
            _sales_earning = float(row_list[1])
            _l_datetime = datetime.strptime(row_list[0], '%Y-%m-%d %H:%M:%S')
            _date = _l_datetime.strftime('%Y-%m-%d')
            _hour = _l_datetime.hour
            # print(_date, _hour, _sales_earning)
            return _date, _hour, _sales_earning
        else:
            # print("Row does not contains 2 columns", row_list)
            return None

    except ValueError as e:
            # logging.warning("File contains wrong data")
            logging.warning(str(e) + ". Row " + str(row_list))
            pass


def dict_to_report(dict_sale_dict):
    biggest_sales_order = sorted(dict_sale_dict.values())

    dict_to_report_return = []

    for date_key in sorted(dict_sale_dict.keys()):
        key_weekday = datetime.strptime(date_key, '%Y-%m-%d').strftime("%A")

        if dict_sale_dict[date_key] == biggest_sales_order[-1]:
            dict_to_report_return.append([date_key, dict_sale_dict[date_key], key_weekday, True])
        else:
            dict_to_report_return.append([date_key, dict_sale_dict[date_key], key_weekday, False])

    return dict_to_report_return


def main(file_name):
    try:
        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            date_sales_dict = {}

            for row in reader:
                # print(row)
                date_hour_earnings = date_hour_sales_entry(row)

                if date_hour_earnings:
                    date_key, hour_key, sales_earnings = date_hour_earnings

                    if date_key not in date_sales_dict:
                        date_sales_dict[date_key] = sales_earnings
                        # date_sales_dict[date_key] = [sales_earnings]
                    else:
                        date_sales_dict[date_key] += sales_earnings
                        # date_sales_dict[date_key].append(sales_earnings)

            # print(date_sales_dict)
            if date_sales_dict:
                list_report = dict_to_report(date_sales_dict)
                # print(list_report)
                for i in list_report:
                    if i[-1]:
                        print("{date_key} - {day_of_week} - {earnings_per_day:.2f} - {biggest_sales_notes}".
                              format(date_key=i[0],
                                     earnings_per_day=i[1],
                                     day_of_week=i[2],
                                     biggest_sales_notes="the most productive day"))
                    else:
                        print("{date_key} - {day_of_week} - {earnings_per_day:.2f}".
                              format(date_key=i[0],
                                     earnings_per_day=i[1],
                                     day_of_week=i[2]))
            else:
                logging.warning("File is empty or does not contain any csv data")

    except FileNotFoundError as e:
        logging.warning("{}".format(e))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        main(filename)
    else:
        print("Usage: {} <file>".format(sys.argv[0]))
