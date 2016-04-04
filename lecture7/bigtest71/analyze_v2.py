#!/usr/bin/env python3 -tt

import os
import sys
from reports import print_summary
from reports import print_category_report
from reports import print_city_report
from reports import print_date_hour_report
from sales import load_sale_data
from catalog import load_catalog_by_item_id


def main():

    try:
        file_catalog, file_sales = _parse_cmd_line_arg()

        sales = load_sale_data(file_sales)
        print_summary(sales)

        catalog_by_item_id = load_catalog_by_item_id(file_catalog)
        # TODO: calculate and print sales report per category
        print_category_report(catalog_by_item_id, sales)

        # TODO: calculate and print sale report per city
        print_city_report(sales)

        # TODO: calculate and print sales report per date-hour
        print_date_hour_report(sales)

        return 0
    except Exception as e:
        print("Error: " + str(e))
        return 1


def _parse_cmd_line_arg():

    if len(sys.argv) != 3:
        raise ValueError("Usage: {} catalogue.csv sale-report.csv".format(sys.argv[0]))

    file_catalog = sys.argv[1]
    file_sales = sys.argv[2]

    if not os.access(file_catalog, os.R_OK) or not os.path.isfile(file_catalog):
        raise ValueError("File {} does not exits or not readable".format(file_catalog))

    if not os.access(file_sales, os.R_OK) or not os.path.isfile(file_sales):
        raise ValueError("File {} does not exits or not readable".format(file_sales))

    result = file_catalog, file_sales
    return result


if __name__ == "__main__":
    sys.exit(main())
