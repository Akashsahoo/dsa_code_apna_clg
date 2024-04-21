def max_sub_arrays_sum(arr):
    max_sum = -99999
    for i in range(len(arr)):
        print(f"sub arrays of {arr[i]} =>")
        for j in range(i,len(arr)):
            print("[",end="")
            total = 0
            for k in range(i,j+1):
                total += arr[k]
                print(arr[k],end=",")
            if (total > max_sum):
                max_sum = total
            print("]",end=" ")
        print()
    print(f" max sum of subarrays => {max_sum}")
li = [1,-2,3,-4]
max_sub_arrays_sum(li)