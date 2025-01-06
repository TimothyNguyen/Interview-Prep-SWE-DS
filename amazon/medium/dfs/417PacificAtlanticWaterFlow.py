class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(reachable_set, r, c):
            if (r,c) in reachable_set or r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
                return
            reachable_set.add((r, c))
            temp_val = heights[r][c]
            heights[r][c] = float('inf')
            if r == 0 or temp_val <= heights[r-1][c]:
                dfs(reachable_set, r-1, c)
            if c == 0 or temp_val <= heights[r][c-1]:
                dfs(reachable_set, r, c-1)
            if r == len(heights) - 1 or temp_val <= heights[r+1][c]:
                dfs(reachable_set, r+1, c)
            if c == len(heights[0]) - 1 or temp_val <= heights[r][c + 1]:
                dfs(reachable_set, r, c + 1)
            heights[r][c] = temp_val

        for c in range(len(heights[0])):
            dfs(pacific_reachable, 0, c)
            dfs(atlantic_reachable, len(heights) - 1, c)
        for r in range(len(heights)):
            dfs(pacific_reachable, r, 0)
            dfs(atlantic_reachable, r, len(heights[0]) - 1)

        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    res.append((r, c))
        return res