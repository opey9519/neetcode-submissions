class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = [-1] * N

        def dp(i):
            # Base Case: Too far or have already robbed
            if i >= N:
                return 0
            # We have seen this house before, return its value
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            return memo[i]
        
        return dp(0)
        
