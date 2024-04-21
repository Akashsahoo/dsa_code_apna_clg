def increasing_order(n):
    if n==1:
       print(n,end=" ")
       return
    increasing_order(n-1)
    print(n,end=" ")
    
increasing_order(10)