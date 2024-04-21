def pairsum(arr,target):
    lp = 0
    rp = len(arr)-1
    while lp!=rp:
        if arr[lp]+arr[rp]==target:
            return True
        elif arr[lp]+arr[rp] > target:
            rp = rp-1
        else:
            lp = lp+1
    return False

arr = [1,2,3,4,5,6]
print(pairsum(arr,19))