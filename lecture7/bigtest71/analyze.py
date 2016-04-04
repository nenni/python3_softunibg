#!/usr/bin/env python3 -tt

"""
Задача: 3. Анализ на данни от верига магазини
Разполагаме с каталог на стоки и данни за продажби на голям производител на спортни стоки,
и трябва да направим анализ на тази информация.

Крайната цел на задачата е да анализираме данните и да визуализираме:
$ python3    analyze.py   catalog.csv   sales-10K.csv

Обобщение
---------
    Общ брой продажби: 10000
    Общо сума продажби: 3191507.82 €
    Средна цена на продажба: 319.150782 €
    Начало на период на данните: 2015-12-01 07:00:48+00:00
    Край на период на данните: 2016-01-24 20:49:38+00:00

Сума на продажби по категории
-----------------------------
    Обувки за футбол : ********************** 912.30 €
    Тениски          : ********* 420.19 €
    Якета            : **************************** 1250.23 €
    Топки            : ************ 502.52 €
    Екипи            : ************** 513.45 €

Сума на продажби по градове
---------------------------
    Франкфурт : ********************** 912.30 €
    Виена     : ********* 420.19 €
    Берлин    : **************************** 1250.23 €
    Марсилия  : ************ 502.52 €
    Париж     : ************** 513.45 €

Часове с най-голяма сума продажби (top 5)
-----------------------------------------
    2016-02-20 18:00 : ********************** 912.30 €
    2016-02-20 19:00 : ********* 420.19 €
    2016-02-20 20:00 : **************************** 1250.23 €
    2016-02-20 21:00 : ************ 502.52 €
    2016-02-20 22:00 : ************** 513.45 €
Обърнете внимание, че часът от последния анализ трябва да бъде в българската часова зона - "+02:00".

"""

import os
import sys
import csv
import iso8601
import pytz
from datetime import datetime


def main():
    if len(sys.argv) != 3:
        print("Usage: {} catalogue.csv sale-report.csv".format(sys.argv[0]))
        return 1

    try:
        catalog_file = sys.argv[1]
        sale_report_file = sys.argv[2]

        if os.access(catalog_file, os.R_OK) and os.path.isfile(catalog_file) \
                and os.access(sale_report_file, os.R_OK) and os.path.isfile(sale_report_file):

            catalog = load_catalog(catalog_file)

            sale_report = load_sale_report(sale_report_file)
            common_report = create_common_report(sale_report)

            print("""Обобщение
{separator}
                Общ брой продажби: {sale_count}
                Общо сума продажби: {total_sales:.2f} €
                Средна цена на продажба: {average_sales:.6f} €
                Начало на период на данните: {start_datetime}
                Край на период на данните: {end_datetime}
                """.format(sale_count=common_report[0],
                           total_sales=common_report[1],
                           average_sales=common_report[2],
                           start_datetime=common_report[3],
                           end_datetime=common_report[4],
                           separator=str('-' * 10)))

    except Exception as e:
        print("Invalid input files provided! Error: " + str(e))
        return 2

    return 0

def load_catalog(filename):
    with open(filename) as f:
        input_data = csv.reader(f)
        return list(input_data)


def load_sale_report(filename):
    with open(filename) as f:
        input_data = csv.reader(f)
        return list(input_data)


def create_common_report(sale_report):

    result = []
    if len(sale_report) > 0:

        total_sales = 0
        start_dt = None
        last_dt = None

        for sales in sale_report:
            total_sales += float(sales[-1])

            current_dt = pytz.UTC.normalize(iso8601.parse_date(sales[-2]))

            if last_dt is None and start_dt is None:
                start_dt = last_dt = current_dt

            else:
                if start_dt > current_dt:
                    start_dt = current_dt

                if last_dt < current_dt:
                    last_dt = current_dt

        average_sales = total_sales / len(sale_report)
        result = [len(sale_report), total_sales, average_sales, str(start_dt), str(last_dt)]
        # print(result)

    return result


if __name__ == "__main__":
    sys.exit(main())
