class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Track seen numbers
        seen = set()

        for num in nums:
            # If num has been seen before -> Contains Duplicate
            if num in seen:
                return True
            # Add number to seen pile
            seen.add(num)
        
        # No duplicates
        return False