li = [1,-2,3,-4]

max_sum = -99999999
total_sum = 0
for i in li:
    total_sum += i
    if max_sum < total_sum:
        max_sum = total_sum
    if total_sum < 0:
        total_sum = 0
print(max_sum)
