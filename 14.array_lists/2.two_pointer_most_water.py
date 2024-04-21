def most_water(heights):
    store_water = 0
    lp = 0
    rp = len(heights)-1
    while lp < rp:
            height = min(heights[lp],heights[rp])
            width = rp-lp
            store_water = max(store_water,height*width)
            if heights[lp] < heights[rp]:
                lp=lp+1
            else:
                rp=rp-1
    return store_water

heights = [1,8,6,2,5,4,8,3,7]
print(most_water(heights))