def sum_n_natural_numbers(n):
    if n==1:
        return 1
    fnm1 = sum_n_natural_numbers(n-1)
    
    fn =n + fnm1
    return fn

print(sum_n_natural_numbers(10))