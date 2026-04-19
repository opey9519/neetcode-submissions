class Solution:
    def isValid(self, s: str) -> bool:
        # Used to compare against stack
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        # Stack
        stack = []

        # Loop through s, compare open to close brackets
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

