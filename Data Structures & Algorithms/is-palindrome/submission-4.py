class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for c in s:
            # characters must be alphanumeric
            if c.isalnum():
                # send c to lowercase for comparison and consistency
                newS += c.lower()
        
        return newS == newS[::-1]