activity_start = [0,1,3,5,5,8]
activity_end = [6,2,4,7,9,9]
activities = []
for i in range(len(activity_start)):
    activity = []
    activity.append(i)
    activity.append(activity_start[i])
    activity.append(activity_end[i])
    activities.append(activity)


activities = sorted(activities,key=lambda x:x[2])
max_act = 0
ans = []
max_act = 1
ans.append(activities[0][0])
end_time = activities[0][2]
for i in range(1,len(activities)):
    if activities[i][1]>=end_time:
        max_act +=1
        ans.append(activities[i][0])
        end_time = activities[i][2]

print(f"all activity {max_act}")

for i in ans:
    print(f"A{i} ",end=" ")