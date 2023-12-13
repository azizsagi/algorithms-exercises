# Coding exercise
# Best time to buy and sell stocks Calculation

stocks = [9, 1, 5, 7, 6, 3, 8, 4]

def calculate(stocks):
    #Logic Buy at lowest point and Sell at highest point - simple :)

    profit = 0               #didn't buy or sell anything yet
    min_stock = stocks[0]

    for i in stocks:
        min_stock = min(min_stock, i)
        profit = max(profit, i - min_stock)
    return profit


print(calculate(stocks))

# Enjoy