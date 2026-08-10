class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # Set up Prefix & Suffix Arrays
        pref = [0] * N
        suff = [0] * N
        pref[0] = suff[-1] = 1
        res = [0] * N
        
        # Create Prefix Product Array
        for i in range(1, N):
            pref[i] = pref[i - 1] * nums[i - 1]
        # Create Suffix Product Array
        for i in range(N - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        # Create Product Except Self Array (Pref * Suff)
        for i in range(N):
            res[i] = suff[i] * pref[i]
        
        return res