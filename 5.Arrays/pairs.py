def pairs(numbers):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            print(f"({numbers[i]},{numbers[j]})",end=" ")
        print()
li = [1,2,3,4,5]
pairs(li)