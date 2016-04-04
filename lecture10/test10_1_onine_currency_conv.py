import requests
from decimal import Decimal
import sys
from pprint import pprint

TARGET_CURRENCY = "BGN"
API_TIMEOUT = 20
API_CURRENCY_EXCHANGE_RATES_URL = 'http://api.fixer.io/latest'


def main():
    # get the input from the user
    original_currency = input("Въведете валута: ")
    original_amount_str = input("Въведете сума: ")
    original_amount = Decimal(original_amount_str)

    # print("... izvli4ane na danni ...")
    response = requests.get(
        API_CURRENCY_EXCHANGE_RATES_URL,
        params={'base': TARGET_CURRENCY},
        timeout=API_TIMEOUT
    )

    exchange_rate_info = response.json()

    # pprint(exchange_rate_info)
    # format:
    # {
    #     "base": "BGN",
    #     "date": "2016-02-04",
    #     "rates": {
    #         "AUD": 1.3873,
    #         "BGN": 1.7453,
    #         "BRL": 3.8806,
    #         "CAD": 1.3712,
    #         . . . .
    exchange_rate = exchange_rate_info.get('rates', {})
    exchange_rate_orig_to_target_currency = exchange_rate.get(original_currency, None)

    if exchange_rate_orig_to_target_currency:
        result = original_amount / Decimal(exchange_rate_orig_to_target_currency)
    else:
        print("Няма информация за валута {}".format(original_currency))
        return 1

    # print()
    print("Равностойност в {}: {:.2f}".format(
        TARGET_CURRENCY,
        result
    ))
    print("exchange rate from {} to {} is: {}".format(original_currency, TARGET_CURRENCY, exchange_rate_orig_to_target_currency))

if __name__ == "__main__":
    sys.exit(main())


