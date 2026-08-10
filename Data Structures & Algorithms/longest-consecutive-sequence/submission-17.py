class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        # Duplicates are irrelevant
        numSet = set(nums)

        for num in numSet:
            length = 0
            # Find a potential sequence starter
            if num - 1 not in numSet:
                # While sequence is true
                while num + length in numSet:
                    length += 1
            # Update max sequence
            longest = max(longest, length)
            
        return longest