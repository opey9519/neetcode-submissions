class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        N = len(nums)
        '''
        Two Paths:
            False = 1st house not robbed, check memo[i][0]
            True = 1st house was robbed, check memo[i][1]
        '''
        memo = [[-1] * 2 for _ in range(N)]
        
        def dp(i, flag):
            # Base Case: Out of bounds & if robbed first cannot rob last
            if i >= N or (flag and i == N - 1):
                return 0
            # If position has been checked, return
            if memo[i][flag] != -1:
                return memo[i][flag]
            # Update value + path with maximum 
            memo[i][flag] = max(nums[i] + dp(i + 2, flag), dp(i + 1, flag))
            return memo[i][flag]
        
        return max(dp(0, True), dp(1, False))
            
