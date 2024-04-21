def pairsum(arr,target):
    
    i = 0
    while arr[i]<arr[i+1]:
        i=i+1
    lp = i+1
    rp = i
    n = len(arr)
    while lp!=rp:
        if arr[lp]+arr[rp]==target:
            return True
        elif arr[lp]+arr[rp] > target:
            rp = (n+rp-1)%n
        else:
            lp = (lp+1)%n
    return False

arr = [11,15,6,8,9,10]
print(pairsum(arr,21))