class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # If nums[l] <= nums[mid], explore left side of array
            if nums[l] <= nums[mid]:
                # If target doesn't reside within [l, mid] -> move to right side 
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # If target resides within [l, mid] -> move to left side
                else:
                    r = mid - 1
            # If nums[l] > nums[mid], explore right side of array
            else:
                # If target doesn't reside within [mid, r] -> move to left side
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # If target resides within [mid, r] -> move to right side
                else:
                    l = mid + 1

        return -1