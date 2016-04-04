#!/usr/bin/env python3 -tt

import sys
from collections import OrderedDict
import csv

from pprint import pprint


file_name = 'sales_data_1.csv'


def main():
    try:

        item_cities_dict = _load_sale_data(file_name)
        # pprint(item_cities_dict)
        city_items = {}
        for item_id, cities in item_cities_dict.items():
            if len(cities) == 1:
                # print(item_id, cities)
                city = str(list(cities)[0])
                # print(city)
                if not city_items.get(city, None):
                    city_items[city] = []
                city_items[city].append(item_id)
        # print(city_items)

        city_items_od = OrderedDict(sorted(city_items.items(), key=lambda t: t[0]))

        if city_items_od:
            for city, items in city_items_od.items():
                items.sort()
                print("{},{}".format(city, ",".join(items)))
        else:
            print("NO UNIQUE SALES")

        return 0

    except Exception as e:
        print("INVALID INPUT", str(e))
        return 1


def _load_sale_data(file_input):

    # all_items = set()
    items_city_dict = {}  # dict key date, value set of city names

    with open(file_input, encoding='utf-8') as f:
        reader = csv.reader(f)
        for sale_row in reader:
            # print(sale_row)
            if sale_row:
                if len(sale_row) == 5:
                    # print(sale_row)
                    item_id = str(sale_row[0])
                    country = str(sale_row[1])
                    city_name = str(sale_row[2])
                    dt = str(sale_row[3])
                    amount = float(sale_row[4])

                    if item_id not in items_city_dict.keys():
                        items_city_dict[item_id] = set()

                    items_city_dict[item_id].add(city_name)
                    # all_items.add(item_id)
                else:
                    raise ValueError

        # pprint(city_items_dict)
        # pprint(all_items)

    if items_city_dict:
        result = items_city_dict
    else:
        raise ValueError("Empty file")

    return result


if __name__ == '__main__':
    sys.exit(main())
