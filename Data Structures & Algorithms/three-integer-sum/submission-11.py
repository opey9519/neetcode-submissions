class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # Cannot sum to 0 if we encounter positive number since array is sorted
            if a > 0:
                break
            # Ensure no dupes
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        
        return res