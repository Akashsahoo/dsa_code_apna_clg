from collections import deque
stack = deque()

def stock_span(stocks,span):
    span.append(1)
    stack.append(0)
    for i in range(1,len(stocks)):
        while len(stack) and stocks[stack[len(stack)-1]] <= stocks[i]:
            stack.pop()
        if not len(stack):
            span.append(i+1)
        else:
            span.append(i-stack[len(stack)-1])
        stack.append(i)
    

stocks = [100,80,60,70,60,85,100]
span = []
stock_span(stocks,span)
print(span)