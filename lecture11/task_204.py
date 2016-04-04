#!/usr/bin/env python3 -tt

import sys
import csv
import iso8601
from datetime import datetime, timezone
from decimal import Decimal


def main():
    try:
        # item_id = input()
        item_id = '741394'
        # file_sales = input()
        file_sales = 'data204/sales_10K.csv'
        sales = load_sale_data(file_sales, item_id)

        item_cities_amounts = []
        for sale in sales:
            if sale.item_id == item_id:
                # print(sale)
                item_cities_amounts.append((sale.city, sale.price))

        # print(item_cities_amounts[:5])
        item_cities_amounts.sort(key=lambda x: x[1])
        # print(item_cities_amounts[:5])
        city_amount_min = item_cities_amounts[0]
        print(city_amount_min[0])

        return 0
    except Exception as e:
        print("INVALID INPUT")
        return 1


class Item(object):

    def __init__(self, item_id, country, city, sale_timestamp, price):
        self.item_id = str(item_id)
        self.country = str(country)
        self.city = str(city)

        if not isinstance(sale_timestamp, datetime):
            self.sale_timestamp = iso8601.parse_date(str(sale_timestamp))
        else:
            self.sale_timestamp = sale_timestamp

        if self.sale_timestamp.tzinfo is None:
            raise ValueError("Error: Naive datetime is not supported")
        else:
            self.sale_timestamp = self.sale_timestamp.astimezone(timezone.utc)

        self.price = Decimal(price)

    def __repr__(self):
        return "Item: " + str(self.__dict__)


def load_sale_data(input_sale_file, item_key):
    with open(input_sale_file) as f:
        sale_data = csv.reader(f)
        sales = []
        for sale_row in sale_data:
            if len(sale_row) and sale_row[0] == item_key:
                sales.append(Item(
                    item_id=sale_row[0],
                    country=sale_row[1],
                    city=sale_row[2],
                    sale_timestamp=sale_row[3],
                    price=sale_row[4]
                ))
        # print(sales[:4])
        return sales


if __name__ == "__main__":
    sys.exit(main())


