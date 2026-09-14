class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            # Base Case: We have no more needed coins
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dp(amount - coin))

            memo[amount] = res
            return res
        
        minCoins = dp(amount)
        return -1 if minCoins >= 1e9 else minCoins

            
