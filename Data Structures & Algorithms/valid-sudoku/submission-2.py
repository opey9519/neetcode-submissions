class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Collection of hashsets to track seen values
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        # Check each number in slot
        for r in range(9):
            for c in range(9):
                # If empty, skip
                if board[r][c] == ".":
                    continue
                
                # If duplicate found, return false
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # Update board if no dupes
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c]) # Squares are calculated in floor division of thirds
        
        return True