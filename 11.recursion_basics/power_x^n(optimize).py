def power(x,n):
    if n==0:
        return 1
    pow = power(x,n//2)
    if n%2:
        return x*pow*pow
    return pow*pow

print(power(2,8))