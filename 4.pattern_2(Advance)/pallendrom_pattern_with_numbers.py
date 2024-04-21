def pallendrom_with_numbers(n):
    for line in range(1,n+1):
        # for spaces
        for _ in range(1,n-line+1):
            print(" ",end="")
        # for numbers 
        for number in range(line,0,-1):
            print(f"{number}",end="")
        for number in range(2,line+1):
            print(f"{number}",end="")
        print()

pallendrom_with_numbers(5)