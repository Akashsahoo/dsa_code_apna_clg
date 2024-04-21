def hollow_rhombus(n):
    for line in range(1,n+1):
        # for spaces
        for _ in range(1,n-line+1):
            print(" ",end="")
        for col in range(1,n+1):
            if line==1 or line==5 or col==1 or col==5:
                print("*",end="")
            else:
                print(" ",end="")
        print()
hollow_rhombus(5)