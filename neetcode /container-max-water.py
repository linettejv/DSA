class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0

        # two pointers l end, right end. 
        # area if W x H
        l, r = 0, len(heights) - 1
        while l < r :
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            # pointer updations:
            if heights[l] < heights[r]:
                l += 1
            else : 
                r -= 1
        return res            
        