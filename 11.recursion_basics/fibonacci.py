def fibonacci(n):
    if n==0 or n==1:
       return n 
    fnm1 = fibonacci(n-1)
    fnm2 = fibonacci(n-2)
    fn = fnm1 + fnm2
    return fn
print(fibonacci(5))