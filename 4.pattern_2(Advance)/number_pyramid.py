def number_pyramid(n):
    for i in range(1,n+1):
        # for spaces
        for _ in range(1,n-i+1):
            print(" ",end="")
        # for numbers
        for _ in range(1,i+1):
            print(f"{i} ",end="")
        print()
number_pyramid(5)
