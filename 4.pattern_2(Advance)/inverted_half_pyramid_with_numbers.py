def inverted_half_pyramid_with_numbers(n):
    for line in range(1, n+1):
        # for numbers
        for number in range(1, n-line+2):
                print(number, end="")
        print()


inverted_half_pyramid_with_numbers(5)
