class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            Inputs: nums: array of integers; target: integer
            Output: array of integers
        '''

        hmap = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in hmap:
                return [hmap[need], i]
            
            hmap[nums[i]] = i
        