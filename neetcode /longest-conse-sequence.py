class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert to set for lookup :
        nums_list = set(nums)
        max_seq = 0
        # which numbers start an interval? 
        for num in nums_list: 
            streak = 1
            next_num = 0
            if num - 1 in nums_list:
                pass
            else:
                next_num = num + 1
                while next_num in nums_list :
                    streak += 1
                    next_num+= 1
                max_seq = max(max_seq, streak)
        return max_seq            




        # Notes : errors faced -> 
        # syntax error, and the streak was off by 1. 
        # Major logic here is : we found elements that were suitable to the intervel starters and then counted their 
        # sequenece length
        # 
        # Concept : 
        # Set searching is o(1) ativity.  