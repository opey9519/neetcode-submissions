class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Track where value occurs
        hmap = {}

        # Pass through, find indexes, update hmap if not found
        for i in range(len(nums)):
            need = target - nums[i]

            if need in hmap:
                return [hmap[need], i]
            
            hmap[nums[i]] = i