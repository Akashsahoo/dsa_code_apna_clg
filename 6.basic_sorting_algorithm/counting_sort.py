def counting_sort(arr):
    print(arr)
    max_elem = -99999
    for i in arr:
        if max_elem < i:
            max_elem = i
    freq_arr = [0]*(max_elem+1)
    for i in arr:
        freq_arr[i] += 1
    
    i =0
    k=0
    while i < len(freq_arr):
        while freq_arr[i]>0:
                arr[k] = i
                k += 1
                freq_arr[i] -=1 
        i = i+1
    print(arr)



arr = [1,4,1,3,2,4,3,7]
counting_sort(arr)