# three sum, target = 0
def threeSum(nums):
    # step one sort the array 
    nums.sort()
    # a place to store the result
    result = []
    
    # this will be a o(n^2) solution
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            # skip duplicates, continue goes to the next iteration 
            continue
        # two pointer logic
        l,r = i + 1, len(nums) - 1

        while l < r: 

            sum = a + nums[l] + nums[r]

            if sum > 0:
                r -= 1
            elif sum < 0: 
                l += 1  
            else :
                result.append([a,nums[l],nums[r]] )  

                # increment pointer l so that it avoids duplicates. 
                l   += 1
                while nums[l] == nums[l - 1] and l < r : l += 1  

    return result

print(threeSum([-1,0,1,2,-1,-4]))


# question : explain the dedup operation in line 30 