#!/usr/bin/env python3 -tt

import sys
import csv
from decimal import Decimal


def main():
    try:
        # item_id = input()
        item_id = '741394'
        item_id.split()
        # file_sales = input()
        file_sales = 'data204/sales_10K.csv'
        file_sales.split()

        city_name = load_data_return_city(file_sales, item_id)
        if city_name:
            print(city_name)
        else:
            raise ValueError

        return 0
    except Exception as e:
        print("INVALID INPUT") #, str(e))
        return 1


def load_data_return_city(input_sale_file, item_key):
    """
    Input sale file name, item_key. Return city name string
    :param input_sale_file:
    :param item_key:
    :return:
    """
    with open(input_sale_file) as f:
        sale_data = csv.reader(f)
        price_min = Decimal("Infinity")
        city_name = None
        # print(type(sale_data))
        # print(list(sale_data)[:5])
        for sale in sale_data:
            sale_item_id = sale[0]
            sale_city = sale[2]
            sale_item_amount = Decimal(sale[4])

            if sale_item_id == item_key:
                if sale_item_amount < price_min:
                    city_name = sale_city
                    price_min = sale_item_amount

    return city_name


if __name__ == "__main__":
    sys.exit(main())



