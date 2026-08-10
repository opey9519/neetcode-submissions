class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Defaults empty key-value pairs to a list
        hmap = defaultdict(list)

        for s in strs:
            # Track char occurence per string
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            # Insert anagram to group
            hmap[tuple(charCount)].append(s)
        
        return list(hmap.values())