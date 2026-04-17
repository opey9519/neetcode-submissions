class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two Pointer Approach + Profit Tracking
        l = 0
        r = 1
        p = 0

        # Iterate through array, comparing l & r pointers
        while r < len(prices) and l <= r:
            # If loss, move day
            if prices[r] < prices[l]:
                l = r
            else:
                p = max(p, prices[r] - prices[l])
                
            r += 1
        
        return p 
            

            
