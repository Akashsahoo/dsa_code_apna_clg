def binary_search(numbers,key):
   lb = 0
   ub = len(numbers)-1
   while lb <=ub:
    mb = (lb+ub)//2
    if key > numbers[mb]:
        lb = mb+1
    elif key < numbers[mb]:
        ub = mb -1
    else:
        return mb


li = [1,2,3,4,5,6,7,8,9]
index = binary_search(li,9)
print(index)