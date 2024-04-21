def most_water(heights):
    store_water = 0
    for i in range(len(heights)):
        for j in range(i+1,len(heights)):
            height = min(heights[i],heights[j])
            width = j-i
            store_water = max(store_water,height*width)
    return store_water

heights = [1,8,6,2,5,4,8,3,7]
print(most_water(heights))


