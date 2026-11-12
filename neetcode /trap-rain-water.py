class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 3:
            return 0

        # two pointers, area
        max_l , max_r = height[0],height[len(height) - 1] 
        area = 0
        l ,r  = 0,len(height) - 1 
        # movement is based on max lengths. not current height!!!
        while l < r:
            if max_r < max_l :
                r -= 1
                water = max_r - height[r]
                if water > 0 : area += water
                if height[r] > max_r:
                    max_r = height[r]

            else:
                l += 1
                water = max_l - height[l]
                if water > 0 : area += water
                if height[l] > max_l :
                    max_l = height[l] 
        return area        

        
        