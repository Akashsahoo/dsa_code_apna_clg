def sub_arrays(arr):
    prefix_sum = []
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        prefix_sum.append(total)

    max_sum = -999999
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if i == 0:
                total_sum = prefix_sum[j]
            else:
                total_sum = prefix_sum[j]-prefix_sum[i-1]
            if total_sum > max_sum:
                max_sum = total_sum
        print()
    print(f" max sum sub array => {max_sum}")
li = [1,-2,3,-4]
sub_arrays(li)