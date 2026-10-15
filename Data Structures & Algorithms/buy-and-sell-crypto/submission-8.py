class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Int: prices: Array of integers
            Out: Integer
            Intuition: maximize profit -> Buy - Sell
        '''

        maxP = 0
        l = 0 # Buy date

        for r in range(len(prices)):
            prof = prices[r] - prices[l]
            # If negative, update new buy date 
            if prof < 0:
                l = r
            
            maxP = max(maxP, prof)
        
        return maxP