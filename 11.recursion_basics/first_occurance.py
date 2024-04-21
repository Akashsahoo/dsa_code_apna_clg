def first_occurance(arr,key,index):
    if index==len(arr):
        return -1
    if arr[index]==key:
        return index
    return first_occurance(arr,key,index+1)


li = [1,2,3,4,15,6,7]
print(first_occurance(li,15,0))