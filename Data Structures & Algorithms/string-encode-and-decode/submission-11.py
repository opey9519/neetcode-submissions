class Solution:

    def encode(self, strs: List[str]) -> str:
        # len(string) + delimeter + word
        newS = ""
        for word in strs:
            newS += (str(len(word)) + "#" + word)

        return newS
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        j = 0

        # 5#Hello5#World
        while i < len(s):
            while s[j] != "#":
                j += 1
            
            # Length of word
            wordLength = int(s[i:j])
            # Move i to start of word
            i = j + 1
            # Move j to end of word
            j = i + wordLength
            res.append(s[i:j])
            # Restart
            i = j
        
        return res