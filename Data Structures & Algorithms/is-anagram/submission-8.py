class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Different lengths = not possible, avoid extra work
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}

        # Track occurence of chars in s & t
        for c in s:
            sMap[c] = 1 + sMap.get(c, 0)
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        
        return tMap == sMap