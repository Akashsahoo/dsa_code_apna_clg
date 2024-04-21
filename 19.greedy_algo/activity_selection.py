activity_start = [1,3,0,5,8,5]
activity_end = [2,4,6,7,9,9]

max_act = 0
ans = []
max_act = 1
ans.append(0)
end_time = activity_end[0]
for i in range(1,len(activity_end)):
    if activity_start[i]>=end_time:
        max_act +=1
        ans.append(i)
        end_time = activity_end[i]

print(f"all activity {max_act}")

for i in ans:
    print(f"A{i} ",end=" ")