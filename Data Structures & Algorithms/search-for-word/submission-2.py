class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()

        def dfs(r, c, i):
            # Success Case: We have seen all characters we need
            if i == len(word):
                return True 
            # Base Case: Out of bounds, Not needed character, already seen
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or i >= len(word) or
                word[i] != board[r][c] or (r, c) in seen
            ):
                return False
            
            # Visiting
            seen.add((r, c))
            
            # Success condition: Is this needed and not already seen?
            # Traverse all possible directions
            res = (
                dfs(r + 1, c, i + 1) or 
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or 
                dfs(r, c - 1, i + 1)
            )

            # No longer visiting
            seen.remove((r, c))

            return res 
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False