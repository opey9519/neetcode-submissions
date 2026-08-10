class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += (str(len(word))+ "#" + word)
        return s

    def decode(self, s: str) -> List[str]:
        i = j = 0
        res = []

        while i < len(s):
            # Find delimeter
            while s[j] != "#":
                j += 1
            # Slice length of string (can be >1 digit)
            jump = int(s[i:j])
            # Set up str slice
            i = j + 1 
            j = i + jump
            res.append(s[i:j])
            i = j
        
        return res


