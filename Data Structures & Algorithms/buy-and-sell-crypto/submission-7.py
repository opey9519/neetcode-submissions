class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            p = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            
            maxP = max(maxP, p)
            r += 1
        
        return maxP