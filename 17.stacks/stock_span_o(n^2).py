def stock_span(stocks,span):
    for i in range(len(stocks)):
        j = i-1
        while j>=0 and stocks[j] <= stocks[i]:
            j = j-1
        span.append(i-j)

stocks = [100,80,60,70,60,85,100]
span = []
stock_span(stocks,span)
print(span)