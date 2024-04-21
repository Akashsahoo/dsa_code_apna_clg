def power(x,n):
    if n==0:
        return 1
    fnm1 = power(x,n-1)
    fn = x*fnm1
    return fn

print(power(2,9))