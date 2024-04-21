def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i,n):
            if arr[j]< arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    print(arr)
arr = [4,11,7,2,19,1]
selection_sort(arr)