#!/usr/bin/env python
import sys

current_key = None
price_dict = {}

def print_average_prices():
    for hour, prices in price_dict.items():
        avg_price = sum(prices) / len(prices)
        print('%s\t%s\t%f' % (current_key, hour, avg_price))

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    hour, price = value.split(',', 1)
    price = float(price)

    if key == current_key:
        if hour in price_dict:
            price_dict[hour].append(price)
        else:
            price_dict[hour] = [price]
    else:
        if current_key is not None:
            print_average_prices()
        current_key = key
        price_dict = {hour: [price]}

if current_key:
    print_average_prices()
