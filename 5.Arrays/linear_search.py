def linear_search(numbers,key):
    for i in range(len(numbers)):
        if numbers[i]==key:
            return i
    return -1

li = [1,2,3,4,5,6,7,8,9]
index = linear_search(li,19)
print(index)