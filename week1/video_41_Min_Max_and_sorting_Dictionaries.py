stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

print(max(zip(stocks.values(), stocks.keys())))
print(min(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))