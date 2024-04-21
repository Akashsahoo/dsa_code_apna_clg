def diamond(n):
    for i in range(1,n+1):
        # for spaces
        for _ in range(1,n-i+1):
            print(" ",end="")
        # for stars
        for _ in range(1,2*i-1+1):
            print("*",end="")
        print()
    # for mirror images
    for i in range(n,0,-1):
        # for spaces
        for _ in range(1,n-i+1):
            print(" ",end="")
        # for stars
        for _ in range(1,2*i-1+1):
            print("*",end="")
        print()


diamond(9)