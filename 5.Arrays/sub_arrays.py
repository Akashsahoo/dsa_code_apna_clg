def sub_arrays(arr):
    counter = 0
    for i in range(len(arr)):
        print(f"sub arrays of {arr[i]} =>")
        for j in range(i,len(arr)):
            print("[",end="")
            for k in range(i,j+1):
                print(arr[k],end=",")
            counter += 1
            print("]",end=" ")
        print()
    print(f" number of subarrays => {counter}")
li = [1,2,3,4]
sub_arrays(li)