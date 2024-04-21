def inverted_triangle_star(n):
    for i in range(1,n+1):
        for j in range(1,(n-i+1)+1):
            print("*",end="")
        print()
inverted_triangle_star(4)