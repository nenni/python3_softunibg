#!/usr/bin/env python3 -tt

import sys
from collections import OrderedDict
import iso8601

from pprint import pprint


file_name = 'dt_city_temp.txt'


def main():
    try:

        d_cities, all_city_names = _load_d_cities(file_name)
        # pprint(d_cities)
        # pprint(all_city_names)
        d_cities_to_print = []
        for d, cities in d_cities.items():
            result_cities = sorted(all_city_names - cities)
            # print(result_cities)
            if result_cities:
                d_cities_to_print.append((d, result_cities))

        if d_cities_to_print:
            for d, cities in d_cities_to_print:
                print("{},{}".format(d, ",".join(cities)))
            # pprint(d_cities_to_print)
        else:
            print("ALL DATA AVAILABLE")

        return 0

    except Exception as e:
        print("INVALID INPUT", str(e))
        return 1


def _load_d_cities(file_input):

    all_city_list = set()
    d_cities = {}  # dict key date, value set of city names

    with open(file_input, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                line_list = line.split(',')
                d = str(iso8601.parse_date(line_list[0]).date())
                # print(type(d))
                city_name = line_list[1]

                if d not in d_cities.keys():
                    d_cities[d] = set()

                d_cities[d].add(city_name)
                all_city_list.add(city_name)

        # pprint(d_cities)
        # pprint(all_city_list)

    if d_cities and all_city_list:
        od = OrderedDict(sorted(d_cities.items(), key=lambda t: t[0]))
        # pprint(od)
        result = (od, all_city_list)
    else:
        raise ValueError("Empty file")

    return result


if __name__ == '__main__':
    sys.exit(main())
