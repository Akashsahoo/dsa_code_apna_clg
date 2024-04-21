def merge_sort(arr,lb,ub):
    if lb<ub:
        mb=(lb+ub)//2
        merge_sort(arr,lb,mb)
        merge_sort(arr,mb+1,ub)
        merge(arr,lb,mb,ub)

def merge(arr,lb,mb,ub):
    total_elem = (ub-lb)+1
    temp_arr = [0]*total_elem
    i=lb
    j=mb+1
    k=0
    while i<=mb and j<=ub:
        if(arr[i]<arr[j]):
            temp_arr[k]=arr[i]
            i =i+1
        else:
            temp_arr[k]=arr[j]
            j=j+1
        k=k+1
    while i<=mb:
        temp_arr[k]=arr[i]
        k=k+1
        i=i+1
    while j<=ub:
        temp_arr[k]=arr[j]
        k=k+1
        j=j+1
    
    k=0
    i=lb
    while k<total_elem:
        arr[i]=temp_arr[k]
        i=i+1
        k=k+1



            
arr=[3,8,19,4,57,15,112]
merge_sort(arr,0,6)
print(arr)
