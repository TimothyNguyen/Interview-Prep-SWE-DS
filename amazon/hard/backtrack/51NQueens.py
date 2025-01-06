from collections import defaultdict


class Solution:
    def solveNQueens(self, n: int):
        res = []
        
        def create_board(curr_board):
            res.append(list(curr_board))

        def backtrack(r, c, remaining_n, curr_board):
            if remaining_n == 0:
                create_board(curr_board)
                return

            for i in range(n):
                curr_diagonal = r - c
                anti_diagonal = r + c
                
                                

        row_tracker, col_tracker = defaultdict(set), defaultdict(set)
        diagonal_tracker, antidiagonal_tracker = defaultdict(set), defaultdict(set)
        empty_board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, 0, n, empty_board)
        return res

