def butterfly(n):
    for line in range(1,n+1):
        # for stars
        for _ in range(1,line+1):
            print("*",end="")
        # for spaces
        for _ in range(1,2*(n-line)+1):
            print(" ",end="")
        # for stars
        for _ in range(1,line+1):
            print("*",end="")
        print()
    #  for mirror image
    for line in range(n,0,-1):
         # for stars
        for _ in range(1,line+1):
            print("*",end="")
        for _ in range(1,2*(n-line)+1):
            print(" ",end="")
        for _ in range(1,line+1):
            print("*",end="")
        print()
butterfly(7)
    