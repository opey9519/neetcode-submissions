class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        prefix = suffix = 0

        for i in range(n):
            # Maintain prefix, use 1 if encounter 0
            prefix = nums[i] * (prefix or 1)
            # Maintain suffix, use 1 if encounter 0
            suffix = nums[n - 1 - i] * (suffix or 1)
            # Update maximum product
            res = max(res, max(prefix, suffix))
        
        return res