from math import sqrt
number = int(input("Enter a number!"))
is_prime = True
if number > 2:
    for i in range(2,int(sqrt(number))+1):
        if (number%i == 0):
            is_prime = False
            break
if is_prime:
    print("number is prime")
else:
    print("number is not prime")

