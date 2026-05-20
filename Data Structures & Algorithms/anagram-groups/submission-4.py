class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create hashmap with default list
        hmap = defaultdict(list)

        # Check each word
        for word in strs:
            char_count = [0] * 26
            for c in word:
                # Increment char count 
                char_count[ord(c) - ord('a')] += 1
            
            # Change Char Count array to tuple b/c lists cannot be keys
            hmap[tuple(char_count)].append(word)
        
        # Return sublists
        return list(hmap.values())