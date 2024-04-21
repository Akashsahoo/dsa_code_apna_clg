def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i-1
        curr = arr[i]
        while j >=0 and arr[j]>curr:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = curr
        
    print(arr)
arr = [4,11,7,2,19,1]
insertion_sort(arr)