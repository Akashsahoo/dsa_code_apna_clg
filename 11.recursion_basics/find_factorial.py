def factorial(n):
    if n==1 or n==0:
        return 1
    fnm1 = factorial(n-1)
    fn = n * fnm1
    return fn


print(factorial(5))