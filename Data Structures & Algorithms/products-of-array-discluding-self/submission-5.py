class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pref = [0] * N
        suff = [0] * N
        pref[0] = suff[-1] = 1
        
        # Fill in prefix products
        for i in range(1, N):
            pref[i] = pref[i - 1] * nums[i - 1]
        # Fill in suffix products
        for i in range(N - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        
        res = [0] * N
        for i in range(N):
            res[i] = pref[i] * suff[i]
        
        return res