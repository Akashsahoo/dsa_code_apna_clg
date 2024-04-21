def zero_one_triangle(n):
    
    for line in range(1,n+1):
        for col in range(1,line+1):
            if (line+col)%2 == 0:
                print(1,end="")
            else:
                print(0,end="")
        print()
zero_one_triangle(5)