def trapping_rain_water(heights):
    n = len(heights)
    left_boundary = [-1]*n
    left_boundary[0] = heights[0]
    
    for i in range(1,n):
        left_boundary[i] = max(heights[i],left_boundary[i-1]) 
        
    
    right_boundary = [-1]*n
    right_boundary[n-1] = heights[n-1]
    for  i in range(n-2,-1,-1):
        right_boundary[i] = max(heights[i],right_boundary[i+1])
        

    store_water = 0
    for i in range(n):
        water_level = min(left_boundary[i],right_boundary[i])
        store_water += water_level-heights[i] 
    print(store_water)


heights = [4,2,0,6,3,2,5]
trapping_rain_water(heights)