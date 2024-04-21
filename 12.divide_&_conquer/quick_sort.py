def quick_sort(arr,lb,ub):
    
    if lb<ub:
        pivot_idx = partition(arr,lb,ub)
        quick_sort(arr,lb,pivot_idx-1)
        quick_sort(arr,pivot_idx+1,ub)


def partition(arr,lb,ub):
    pivot = arr[ub]
    i=lb-1
    for j in range(lb,ub):
        if arr[j]<=pivot:
            i=i+1
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    i=i+1
    temp = arr[i]
    arr[i]=arr[ub]
    arr[ub]=temp
    return i     # pivot_index



arr=[3,8,19,4,3,4,57,15,112]
quick_sort(arr,0,6)
print(arr)
