class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        hmap = {} 
        l = 0
        mostFreqChar = 0
        
        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)
            mostFreqChar = max(mostFreqChar, hmap[s[r]])

            while (r - l + 1) - mostFreqChar > k:
                hmap[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest