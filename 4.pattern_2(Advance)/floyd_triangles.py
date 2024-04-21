def floyd_triangle(n):
    counter = 1
    for line in range(1,n+1):
        for _ in range(1,line+1):
            print(f"{counter} ",end="")
            counter +=1
        print()
floyd_triangle(5)