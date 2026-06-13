# find the max area of the container. you are given an array of heights. 
# brute force is to find all the areas possible
# o(n) is 2 pointer method

def maxContainer ( self, heights : list[int]) -> int:
    areaMax = 0
    l = 0 , r = heights[-1]

    while l < r :
        # find the current area -> len * height
        currentArea = ( r - l) * min(heights[l], heights[r])
        areaMax = max( areaMax , currentArea)
        # update the pointer 
        if heights[l] < heights[r]:
            l += 1
        elif heights[l] > heights[r]:
            r -= 1
        else :
            l += 1
    return areaMax                

