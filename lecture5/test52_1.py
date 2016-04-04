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



Разширение на задачата
Разширете кода си, така че да показва в кой час има най-много продажби. Интересува ни часа, а не деня.

Пример: За целия период
между 13:00 и 14:00 е имало продажби за 897 лева,
между 14:00 и 15:00 е имало продажби за 456 лева.
Между 13:00 и 14:00 е имало повече продажби отколкото между 14:00 и 15:00


"""

import sys
import logging
from datetime import datetime
import csv
from pprint import pprint


def date_hour_sales_entry(row_list):
    try:
        if len(row_list) == 2:
            _l_datetime = datetime.strptime(row_list[0], '%Y-%m-%d %H:%M:%S')
            _date = _l_datetime.strftime('%Y-%m-%d')
            _hour = _l_datetime.hour
            _sales_earning = float(row_list[1])
            return _date, _hour, _sales_earning
        else:
            return None

    except ValueError as e:
            logging.warning(str(e) + ". Row " + str(row_list))
            pass


def hour_to_report(date_hours_earnings_dict):

    hours_earnings_dict = {}
    for date_key, hour_earning_value in date_hours_earnings_dict.items():
        # print(date_key, hour_earning_value[0])
        for hour_key, value in dict(hour_earning_value[0]).items():
            # print(hour_key, type(value))
            if hour_key not in hours_earnings_dict:
                hours_earnings_dict[hour_key] = sum(value)
            else:
                hours_earnings_dict[hour_key] += sum(value)

    # pprint(hours_earnings_dict)
    return hours_earnings_dict


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
                        date_sales_dict[date_key] = [{hour_key: [sales_earnings]}]
                    else:
                        for hour_key_value in date_sales_dict[date_key]:
                            # print(hour_key_value)
                            if hour_key not in hour_key_value:
                                hour_key_value[hour_key] = [sales_earnings]
                            else:
                                hour_key_value[hour_key].append(sales_earnings)

            # pprint(date_sales_dict)
            if date_sales_dict:
                # result = date_to_report(date_sales_dict)
                result = hour_to_report(date_sales_dict)
                # result - list of hours - sum(earnings)
                pprint(result)
                highest_hour_earnings = max(result, key=result.get)
                print("The highest earnings are in {hour_var} o'oclock".
                      format(hour_var=highest_hour_earnings))

    except FileNotFoundError as e:
        logging.warning("{}".format(e))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        main(filename)
    else:
        print("Usage: {} <file>".format(sys.argv[0]))
