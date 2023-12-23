import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        already_checked = set()
        tot_islands = 0

        def bfs(r, c):
            land_patch_queue = collections.deque()
            land_patch_queue.append((r, c))
            
            while land_patch_queue:
                r, c = land_patch_queue.popleft()
                adjacent = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
                
                if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == '1' and (r, c) not in already_checked:
                    land_patch_queue.extend(adjacent)
                already_checked.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in already_checked and grid[r][c] == '1':
                    bfs(r, c)
                    tot_islands += 1
        
        return tot_islands