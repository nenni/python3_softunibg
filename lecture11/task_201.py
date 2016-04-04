#!/usr/bin/env python -tt

"""
Реализирайте програма, която да конвертира сума от подадена валута към български лева (BGN).
Резултатите трябва да се закръглят до втория знак след десетичната запетая.

Входни данни:
- име на файл, съдържащ обменни курсове на различни валути към BGN;
Празните редове във файла не бива да се обработват;
- име на файл, съдържащ на всеки ред сума и валута, в която е сумата;
Празните редове във файла не бива да се обработват;
Имайте предвид, че в този файл ще има по няколко суми от една и съща валута;

Очакван изход:
За всеки ред от файла със сумите, трябва да бъде изведена на отделен ред съответната сума в български лева.
"""
import sys
from decimal import Decimal


def main():
    try:
        # file_exchange_rate_to_target = input()
        # file_amount_to_convert_to_target = input()

        file_exchange_rate_to_target = 'data201/exchange.txt'
        file_amount_to_convert_to_target = 'data201/amounts.txt'

        with open(file_exchange_rate_to_target) as f:
            exchange_rate_dict = {}
            for row in f.readlines():
                list_row = row.split()
                if len(list_row) != 0:
                    currency = list_row[0]
                    exchange_rate = Decimal(list_row[1])
                    exchange_rate_dict[currency] = exchange_rate

        with open(file_amount_to_convert_to_target) as f:
            amount_to_convert = []
            for row in f.readlines():
                list_row = row.split()
                if len(list_row) != 0:
                    amount = Decimal(list_row[0])
                    currency = list_row[1]
                    amount_to_convert.append((currency, amount))
            # print(amount_to_convert)

        convert_currency_to_target(exchange_rate_dict, amount_to_convert)

        return 0

    except Exception as e:
        print("INVALID INPUT")
        return 1


def convert_currency_to_target(exchange_rate, currency_amounts):
    for cur_amount in currency_amounts:
        cur_exchange_rate = exchange_rate.get(cur_amount[0], None)
        if cur_exchange_rate and cur_exchange_rate != 0:
            cur_exchange_rate = Decimal(cur_exchange_rate)

            amount_to_target = Decimal(cur_amount[1]) / cur_exchange_rate

            print("{target_amount:.2f}".format(
                target_amount=amount_to_target
            ))

if __name__ == "__main__":
    sys.exit(main())
