class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Maximize the Distance between 2 bars
        # Maximize the Height of 2 bars 

        l = 0
        r = len(heights) - 1
        maxVol = 0

        while l < len(heights) and l < r:
            curVol = (r - l) * (min(heights[r], heights[l]))
            maxVol = max(maxVol, curVol)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        
        return maxVol