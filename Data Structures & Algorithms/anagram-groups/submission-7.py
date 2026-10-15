class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for word in strs:
            charArr = [0] * 26
            for c in word:
                charArr[ord(c) - ord('a')] += 1
            
            hmap[tuple(charArr)].append(word)
        
        return list(hmap.values())