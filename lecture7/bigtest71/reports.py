from datetime import datetime, timezone
from decimal import Decimal
from pprint import pprint


def print_summary(sales):

    total_count = len(sales)
    total_sales_amount = Decimal(0)
    sales_timestamp_min = datetime.max.replace(tzinfo=timezone.utc)
    sales_timestamp_max = datetime.min.replace(tzinfo=timezone.utc)

    for sales_item in sales:
        total_sales_amount += sales_item.price

        if sales_item.sale_timestamp < sales_timestamp_min:
            sales_timestamp_min = sales_item.sale_timestamp
        if sales_item.sale_timestamp > sales_timestamp_max:
            sales_timestamp_max = sales_item.sale_timestamp

    print("""
Обобщение
----------
Общ брой продажби: {total_count}
Общо сума продажби: {total_sales_amount} €
Средна цена на продажба: {average_sales} €
Начало на период на данните: {start_dt}
Край на период на данните: {end_dt}
""".format(
        total_count=total_count,
        total_sales_amount=total_sales_amount,
        average_sales=total_sales_amount/total_count,
        start_dt=sales_timestamp_min,
        end_dt=sales_timestamp_max
    ))


def print_category_report(catalog_by_item_id, sales):

    category_total_dict = {}
    for sale in sales:
        if sale.item_id in catalog_by_item_id:
            key_category_entry = catalog_by_item_id[sale.item_id]
            key_category_name = key_category_entry.category

            if key_category_name not in category_total_dict:
                category_total_dict[key_category_name] = Decimal(0)

            category_total_dict[key_category_name] += sale.price

    # sales_for_display = [] # empty list, items will be tuples - category_name, amount
    #
    # for category_name, sales_amount in category_total_dict.items():
    #     sales_for_display.append((sales_amount, category_name)) # adding tuples to the list
    # or

    sales_for_display = list(category_total_dict.items())

    # sales_for_display.sort(reverse=True)
    sales_for_display.sort(key=lambda item: item[1], reverse=True)
    # pprint(category_total_dict)
    total_sales_amount = sum(category_total_dict.values())
    # print(total_sales_amount)

    print("""
Сума на продажби по категории (top 5)
-------------------------------------""")

    for category_name, sales_amount in sales_for_display[:5]:
        print("{category:20} : {bar_slide} {amount} €".format(
            category=category_name,
            bar_slide='*' + '*' * int(100*sales_amount/total_sales_amount),
            amount=sales_amount
        ))


def print_city_report(sales):

    city_total_dict = {}
    total_sales_amount = Decimal(0)
    for sale in sales:
        if sale.city not in city_total_dict:
            city_total_dict[sale.city] = Decimal(0)

        city_total_dict[sale.city] += sale.price
        total_sales_amount += sale.price

    # # Variant 1 - list of tuples and sort
    # sales_for_display = []  # empty list, items will be tuples
    # for city, sales_amount in city_total_dict.items():
    #     sales_for_display.append((sales_amount, city)) # adding tuples to the list
    # sales_for_display.sort(reverse=True)

    # Variant 2 - list of tuples and sort
    sales_for_display = list(city_total_dict.items())
    # sales_for_display.sort(reverse=True)
    sales_for_display.sort(key=lambda item: item[1], reverse=True)

    # print(sales_for_display)

    print("""
Сума на продажби по градове (top 5)
------------------------------------""")

    for city, sales_amount in sales_for_display[:5]:
        print("{city:20} : {bar_slide} {amount} €".format(
            city=city,
            bar_slide='*' + '*' * int(100*sales_amount/total_sales_amount),
            amount=sales_amount
        ))


def print_date_hour_report(sales):

    date_hour_total_dict = {}
    total_sales_amount = Decimal(0)
    for sale in sales:

        date_hour_key = sale.sale_timestamp.strftime("%Y-%m-%d %H")

        if date_hour_key not in date_hour_total_dict:
            date_hour_total_dict[date_hour_key] = Decimal(0)

        date_hour_total_dict[date_hour_key] += sale.price
        total_sales_amount += sale.price

    if date_hour_total_dict and total_sales_amount != 0:
        inverse_date_hour_total_dict = {v: k for k, v in date_hour_total_dict.items()}

        print("""
Часове с най-голяма сума продажби (top 5)
-----------------------------------------""")

        for _ in range(5):

            max_hour_sales = inverse_date_hour_total_dict.pop(max(inverse_date_hour_total_dict, default=None), None)

            if max_hour_sales is not None:
                sales_per_hour = date_hour_total_dict[max_hour_sales]

                print("{date_hour}:00 : {bar_slide} {amount} €".format(
                    date_hour=max_hour_sales,
                    bar_slide='*' + '*' * int(100*sales_per_hour/total_sales_amount),
                    amount=sales_per_hour
                ))
        print()
