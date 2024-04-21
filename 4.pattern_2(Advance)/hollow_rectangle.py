def hollow_rectangle(n):
    for i in range(1, n+1):
        for j in range(1, 6):
            if (i == 1 or i == n or j == 1 or j == 5):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


hollow_rectangle(4)
 