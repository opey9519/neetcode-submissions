class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # Identify possible combination sums to reach target
        def backtrack(curArr, curSum, i):
            # Base Case: If target reached, do nothing
            if i == len(nums) or curSum > target:
                return 
            # Target Case: If target met, append arr
            if curSum == target:
                res.append(curArr.copy())
                return
            
            curArr.append(nums[i])
            backtrack(curArr, curSum + nums[i], i)
            curArr.pop()
            backtrack(curArr, curSum, i + 1)
        
        backtrack([], 0, 0)
        return res
            
