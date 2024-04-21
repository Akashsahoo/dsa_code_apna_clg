def solid_rhombus(n):
    for line in range(1,n+1):
        # for spaces
        for _ in range(1,n-line+1):
            print(" ",end="")
        for _ in range(1,n+1):
            print("*",end="")
        print()
solid_rhombus(5)