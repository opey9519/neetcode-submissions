class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for i in range(len(nums)):
            length = 0
            while nums[i] + length in nums:
                length += 1
            
            longest = max(longest, length)
        
        return longest
