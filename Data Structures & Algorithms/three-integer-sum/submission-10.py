class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Since sorted, every value after 0 cannot sum to 0
            if a > 0:
                break
            # Cannot contain duplicates
            if i > 0 and nums[i - 1] == a:
                continue
            
            # Set pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[l] + nums[r] + a

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # Plausible answer
                    res.append([nums[l], nums[r], a])
                    # Move pointers, must be distinct
                    l += 1
                    r -= 1
                    # If duplicates, keep moving
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        
        return res
