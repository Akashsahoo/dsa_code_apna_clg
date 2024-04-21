def stock_max_profit(stocks_price):
    n = len(stocks_price)
    buy_price = stocks_price[0]
    max_profit = -99999999
    profit = 0
    for i in range(1,n):
        if stocks_price[i] > buy_price:
            profit = stocks_price[i] - buy_price
        else:
            buy_price = stocks_price[i]
        if max_profit < profit :
            max_profit = profit
    print(max_profit)

stocks_price = [7,1,5,3,6,4]
stock_max_profit(stocks_price)
        