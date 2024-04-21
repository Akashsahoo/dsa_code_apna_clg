def tilling_problem(n):
    if n==0 or n==1:
        return 1
    
    totalways = tilling_problem(n-1)+tilling_problem(n-2)
    return totalways


print(tilling_problem(3))