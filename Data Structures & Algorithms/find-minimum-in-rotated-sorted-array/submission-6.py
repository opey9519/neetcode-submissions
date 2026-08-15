class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("infinity")
        l = 0
        r = len(nums) - 1

        while l <= r:
            # Edge Case: array/subarray is now sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (r + l) // 2
            res = min(res, nums[mid])
            
            # If midpoint is greater than l, the minimum must be more right
            if nums[mid] >= nums[l]:
                l = mid + 1
            # If midpoint is less than l, the minimum must be more left
            else:
                r = mid - 1

        
        return res