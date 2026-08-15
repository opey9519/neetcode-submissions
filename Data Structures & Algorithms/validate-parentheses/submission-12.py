class Solution:
    def isValid(self, s: str) -> bool:
        # Matching parenthesis
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        # Edge Case: if stack is only open parenthesis, then False
        return True if not stack else False