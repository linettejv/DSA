class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # max length - max freq char  < k -> makes this an invalid string : here we've got to change more than k people. 
        # its a sliding window. 
        # we need to store the count of each char - dict 
        #.values return all the values in a dict 
        count = {}

        res = 0
        l = 0
        # for certain sliding windows -> or say usually, r is given in the for loop. 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            # check valididity :
            while (r - l + 1) - max(count.values()) > k :
                count[s[l]] -= 1
                l += 1
            res = max( res, r - l + 1)

            print(s[l : r-l+1])
            print (res)

        return res        

sol = Solution()
print(sol.characterReplacement("AABABBA",1))        