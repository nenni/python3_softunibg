#!/usr/bin/env python3 -tt

import os
from pprint import pprint
import sys
import sqlite3


def main():

    try:

        db_filename = _parse_cmd_line_arg()

        # city_name = input('Въведете име на град: ')
        city_name = user_input()
        # print(city_name)

        with sqlite3.connect(db_filename, isolation_level=None) as connection:
            # print("Connection opened")
            result = dump_sales_by_city(city_name, connection)
            # dump_sales_by_city(city_name, connection)
        # pprint(result)

        print_city_sales_report(result, city_name)

        return 0
    except Exception as e:
        print("Error: " + str(e))
        return 1


def print_city_sales_report(sales_per_city, city_name):

    if sales_per_city:
        print("Продажби в град {}: ".format(city_name))
        for sale in sales_per_city:
            print("Артикул #: {item_id}   дата/час: {time_stamp}   сума: {sale_amount}".format(
                item_id=sale[0],
                time_stamp=sale[1],
                sale_amount=sale[2]
            ))
        print("Total number of sales per city: {}".format(len(sales_per_city)))

    else:
        print("Няма данни за продажби в град {}.".format(city_name))


def user_input():
    result = input("Въведете име на град: ")
    # TODO validate the user input
    return result


def dump_sales_by_city(city_name, connection):
    cursor = connection.cursor()
    result = cursor.execute(
        """
            select
                item_id,
                sale_timestamp,
                price
            from
                sale
            join
                catalog on catalog.id = sale.catalog_id
            where
                city = (?)
            order by
                sale_timestamp;
        """,
        [
            city_name
        ]
    )

    return list(result)


def _parse_cmd_line_arg():

    if len(sys.argv) != 2:
        raise ValueError("Usage: {} <input.db>".format(sys.argv[0]))

    db_filename = sys.argv[1]

    if not os.access(db_filename, os.R_OK) or not os.path.isfile(db_filename):
        raise ValueError("File {} does not exits or not readable".format(db_filename))

    result = db_filename
    return result


if __name__ == "__main__":
    sys.exit(main())
