class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        #  the first pointer at the leftmost 
        j = len(numbers) - 1
        #  the pointer at the other end. 
        while i < j : 
            #  condition given : distinct indeces. 
            if numbers[i] + numbers[j] > target : 
                j = j - 1
            elif numbers[i] + numbers[j] < target : 
                i = i + 1
            else:
                return([i+1,j+1])

# Notes : 
# pointer decisions lie on both the sides and not one alone. 
# its like a zipper tightening form both ends.                 