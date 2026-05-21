class Solution:

    # Encode and return string
    def encode(self, strs: List[str]) -> str:
        # str = delimeter + len(word) + word
        s = ""
        for word in strs:
            s += f"{len(word)}#{word}"
        
        print(s)
        return s

    # Decode into original list of strings
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        '''
            Find delimeter (start of new word)
            Progress each word via length and save to temp
        '''
        # 5#Hello5#World
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

            
