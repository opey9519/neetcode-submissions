class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        p = 0

        while l <= r and r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                p = max(p, prices[r] - prices[l])
            
            r += 1
        return p