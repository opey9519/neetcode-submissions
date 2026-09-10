class Solution:
    def climbStairs(self, n: int) -> int:
        # Store incremental results
        memo = [-1] * n
        
        def dp(i):
            # Base Case: we went too far, or landed on top
            if i >= n:
                # 1 if we are at top, 0 if we are too far
                return 1 if i == n else 0
            if memo[i] != -1:
                return memo[i]
            
            # Calculate and store intermediate results
            res = dp(i + 1) + dp(i + 2)
            memo[i] = res

            return res
        
        return dp(0)