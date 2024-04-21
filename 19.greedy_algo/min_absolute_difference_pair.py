
def min_absolute_difference_pair(list1,list2):

    list1 = sorted(list1,reverse=True)
    list2 = sorted(list2,reverse=True)

    min_diff = 0
    for i in range(len(list1)):
        min_diff += abs(list1[i]-list2[i])
    print(min_diff)



list1 = [4,1,8,7]
list2 = [2,3,6,5]
min_absolute_difference_pair(list1,list2)