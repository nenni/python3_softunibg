#!/usr/bin/env python3


prices = []

while True:
    current_price_str = input("Insert price or type STOP: ")
    if current_price_str.lower() == 'stop':
        break

    # TODO: check if the current_price_str is valid float
    try:
        prices.append(float(current_price_str))
    except:
        print("Inserted price -- %s -- is not integer or float" % current_price_str)
        pass

print("All prices:")
print(prices)

# TODO: implement average price
if len(prices) < 4:
    print("Please enter at least 4 prices")
else:
    prices.sort()
    print("Sorted prices:")
    print(prices)

    # min_price = prices[0]
    min_price = min(prices)

    print("Min price is: " + str(min_price))
    min_price_count = prices.count(min_price)
    for i in range(min_price_count):
        prices.remove(min_price)

    if len(prices) > 0:
        # max_price = prices[-1]
        max_price = max(prices)
        print("Max price is: " + str(max_price))
        max_price_count = prices.count(max_price)
        for i in range(max_price_count):
            prices.remove(max_price)
    else:
        print("All prices are the same as min price")

    if len(prices) > 0:
        sum_prices = sum(prices)
        print("Average price is: " + str(sum_prices/len(prices)))
    else:
        print("There is no average price. "
              "Only min and/or max prices entered")
