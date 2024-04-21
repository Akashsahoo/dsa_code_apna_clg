def check_array_sorted(arr,n):
    if n==len(arr)-1:
        return True
    if arr[n]<arr[n+1]:
        return check_array_sorted(arr,n+1)
    else:
        return False


li = [1,2,3,4,15,6,7]
print(check_array_sorted(li,n=0))