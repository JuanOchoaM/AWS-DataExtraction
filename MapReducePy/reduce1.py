#!/usr/bin/env python
import sys

def print_average_variability(key, price_differences):
    if price_differences:
        avg_variability = sum(price_differences) / len(price_differences)
        print '%s\t%f' % (key, avg_variability)

current_key = None
current_prices = []
price_differences = []

for line in sys.stdin:
    line = line.strip()
    key, price = line.split('\t', 1)
    price = float(price)

    if key == current_key:
        current_prices.append(price)
    else:
        if current_prices:
            for i in range(1, len(current_prices)):
                difference = abs(current_prices[i] - current_prices[i-1])
                price_differences.append(difference)
            print_average_variability(current_key, price_differences)
        
        current_key = key
        current_prices = [price]
        price_differences = []

if current_prices:
    for i in range(1, len(current_prices)):
        difference = abs(current_prices[i] - current_prices[i-1])
        price_differences.append(difference)
    print_average_variability(current_key, price_differences)
