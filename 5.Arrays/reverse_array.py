def reverse(numbers):
    pointer_1 = 0
    pointer_2 = len(numbers)-1
    while pointer_1 < pointer_2:
        temp = numbers[pointer_2]
        numbers[pointer_2] = numbers[pointer_1]
        numbers[pointer_1] = temp
        pointer_1 = pointer_1+1
        pointer_2 = pointer_2-1

li = [1,2,3,4,5,6,7,8,9]
reverse(li)
print(li)