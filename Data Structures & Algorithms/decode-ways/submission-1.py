class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            # Success Case: Already seen
            if i in dp:
                return dp[i]
            # Base Case: 0 is not legal value (for leading 0's)
            if s[i] == "0":
                return 0
            
            # Subproblem 1: individual chars
            res = dfs(i + 1)
            # Subproblem 2: double-digits
            # The first char must be 1 or 2 and if 2, followed by 0-6
            if (i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and (s[i + 1] in "0123456")
            )):
                res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)