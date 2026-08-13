class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charCount = {}
        maxLength = 0
        maxF = 0

        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            # Track most frequent character
            maxF = max(maxF, charCount[s[r]])

            # (Window length) - Most occured character > Maximum replaceable characters
            # This formula gives the # of least characters which is compared against k
            while (r - l + 1) - maxF > k:
                charCount[s[l]] -= 1
                l += 1
            
            # Update maxLength w/ Window Length
            maxLength = max(maxLength, r - l + 1)
            
        return maxLength