class Solution:
    # Encrypted str: len(s), delimeter (#), str
    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += f"{len(word)}#{word}"
        return s

    # Decrypt by finding len, delimeter, splicing str and appending to res
    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i # Pointer to find delimeter
            
            # Find delimeter
            while s[j] != "#":
                j += 1
            s_len = int(s[i:j]) # Length of word
            
            i = j + 1
            j = i + s_len
            word = s[i : j]
            res.append(word)

            i = j
        
        return res