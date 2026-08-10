class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Track index numbers occur in nums
        hmap = {}

        for i in range(len(nums)):
            # Needed to sum to target
            need = target - nums[i]

            # Success condition
            if need in hmap:
                return [hmap[need], i]
            # Update num and its position
            hmap[nums[i]] = i
        