class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        l = 0
        r = len(heights) - 1

        while l < len(heights) and l < r:
            curMax = (r - l) * (min(heights[l], heights[r]))
            maxW = max(maxW, curMax)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        return maxW