class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base Case: we cannot have a substring s` of t if len(s`) < len(t)
        if t == "":
            return ""

        # Track occurence of chars in t
        tCount, window = {}, {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        # Set up
        # Left Side of Window
        l = 0
        # Have = current chars in s that match chars in t + occurence
        # Need = # of characters needed for Have
        have, need = 0, len(tCount)
        # res = Window indexed
        # resLen = length of window
        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            # Update window tracking
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # If char count in window matches t increment have
            if c in tCount and window[c] == tCount[c]:
                have += 1
            
            # While substring conditions are met, optimize
            while have == need:
                # Update minimum substring
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # If when optimizing, conditions are no longer met, decrement
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        # Extract window slices & return minimum window substring
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""