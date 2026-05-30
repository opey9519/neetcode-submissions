class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix & Suffix Array
        N = len(nums)
        pref = [0] * N
        suff = [0] * N
        arr = [0] * N
        
        # No elements past edge to multiply; therefore 1
        pref[0] = suff[-1] = 1

        # pref[i] = product of elements previous in nums, excluding index i
        for i in range(1, len(nums)):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        # suff[i] = product of subsequent in nums, excluding index i 
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        # arr[i] = product of all elements in nums except index i
        for i in range(N):
            arr[i] = pref[i] * suff[i]
        
        return arr
