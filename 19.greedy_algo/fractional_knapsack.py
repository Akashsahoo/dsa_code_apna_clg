def fractional_knapsack(value,weight,capaity):
    data = []
    for i in range(len(weight)):
        item = []
        item.append(i)
        item.append(value[i])
        item.append(weight[i])
        item.append(value[i]/weight[i])
        data.append(item)

    data = sorted(data,key=lambda x:x[3],reverse=True)
    total_weight = 0
    max_value = 0
    index = 0
    while total_weight < capaity:
          if total_weight + data[index][2]<=capaity:
             total_weight +=data[index][2]
             max_value += data[index][1]
          else:
            max_value +=data[index][3]*(capaity-total_weight)
            total_weight = capaity
          index += 1
    print(max_value)






value = [200,180,300,39]
weight = [20,18,50,13]
capaity = 80
fractional_knapsack(value,weight,capaity)