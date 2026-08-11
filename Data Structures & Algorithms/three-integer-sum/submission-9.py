class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Contains distinct triplets, can be empty if none
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # No longer possible to sum to 0
            if a > 0:
                break
            # No duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum3 = a + nums[l] + nums[r]

                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # While l is a duplicate, increment l
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                    
        
        return res