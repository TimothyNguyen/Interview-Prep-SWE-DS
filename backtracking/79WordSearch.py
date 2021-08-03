class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word is None or len(word) == 0 or board is None or len(board) == 0: return False
        
        def dfs(idx, r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[idx]: return False
            if board[r][c] == word[idx] and idx == len(word) - 1: return True
            else:
                board[r][c] = '*'
                ans = dfs(idx + 1, r + 1, c) or dfs(idx + 1, r - 1, c) or dfs(idx + 1, r, c + 1) or dfs(idx + 1, r, c - 1)
                board[r][c] = word[idx]
                return ans
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0] == board[r][c]:
                    if dfs(0, r, c): return True
        return False