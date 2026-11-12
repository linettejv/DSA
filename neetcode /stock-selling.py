class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        l = 0
        r = 1
        maxpro = 0
        while r < len(prices):
            maxpro = max(maxpro, prices[r]-prices[l])
            if prices[r] < prices[l] :
                l = r
            r += 1
           
        return maxpro    
        