class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Boundaries
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):
            # Success Case: We have hit all letters
            if i == len(word):
                return True
            # Base Case: Out of bounds or not in word
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or
                word[i] != board[r][c] or board[r][c] == "#"
            ):
                return False
            
            # Visited
            board[r][c] = "#"

            # DFS
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Backtrack: restore cell
            board[r][c] = word[i]
            return res

        # Initiate search at each possible location
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False