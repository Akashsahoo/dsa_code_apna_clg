def last_occurance(arr,key,index):
    if index==len(arr):
        return -1

    index1=last_occurance(arr,key,index+1)   
    if arr[index]==key:
        return index1 if index1>index else index
        # if index1>index:
        #     return index1
        # else:
        #     return index
    return index1

li = [1,2,3,4,15,6,7,15]
print(last_occurance(li,15,0))