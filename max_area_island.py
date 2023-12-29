class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global curr_area
        curr_area, max_area = 0, 0
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            global curr_area
            if not (0<=r<row) or not (0<=c<col) or grid[r][c] != 1:
                return
            
            grid[r][c] = -1
            curr_area += 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    curr_area = 0
                    dfs(r, c)
                    max_area = max(max_area, curr_area)
        
        return max_area
        