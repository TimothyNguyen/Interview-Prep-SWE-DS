import collections
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, boxes = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        
        n = len(board)

        # Fill in the data for these defaultdict
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[box_idx].add(board[r][c])

        def is_valid(val, r, c, box_idx):
            return val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]

        def backtracking(r, c):
            if r == len(board) and c == len(board[0]):
                return True
            if c == len(board[0]):
                r += 1
                c = 0

            # Add case where it's filled already - ignore
            if board[r][c] != '.':
                return backtracking(r, c + 1)

            box_idx = (r // 3) * 3 + (c // 3)
            for v in range(1, n + 1):
                if is_valid(v, r, c, box_idx):
                    board[r][c] = str(v)
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[box_idx].add(v)
                    if backtracking(r, c + 1):
                        return True

                    rows[r].remove(v)
                    cols[c].remove(v)
                    boxes[box_idx].remove(v)
                    board[r][c] = '.'
            return False


        backtracking(0, 0)
        return board