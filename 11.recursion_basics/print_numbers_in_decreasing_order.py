def decreasing_order(n):
    if n==1:
       print(n,end=" ")
       return
    print(n,end=" ")
    decreasing_order(n-1)
    
decreasing_order(10)
    