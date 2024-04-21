def inverted_and_rotated_half_pyramid(n):
    for line in range(1, n+1):
        # for spaces
        for _ in range(1, n-line+1):
                print(" ", end="")
        # for stars
        for _ in range(1,line+1):
            print("*",end="")
        print()


inverted_and_rotated_half_pyramid(4)
