def tilling_problem(n):
    if n==1 or n==2:
        return n
    
    totalways = tilling_problem(n-1)+tilling_problem(n-2)
    return totalways


print(tilling_problem(3))