class Solution:
    def isValid(self, s: str) -> bool:
        '''
            Input: s: string of paranthesis type characters
            Output: boolean: is this valid or not
        '''
        # hashmap reference to pair closed to open brackets
        closeToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []

        for c in s:
            if c in closeToOpen and stack:
                if stack[-1] == closeToOpen[c]:
                    # Matching bracket
                    stack.pop()
                else:
                    # Non matching bracket
                    return False
            else:
                # Append open brackets and if stack empty to allow comparison
                stack.append(c)

        return True if not stack else False