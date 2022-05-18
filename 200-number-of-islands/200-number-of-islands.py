class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    self.dfs(grid, y, x)
                    count += 1
        return count
    
    def dfs(self, grid, y, x):
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] != '1':
            return
        grid[y][x] = '#'
        self.dfs(grid, y + 1, x)
        self.dfs(grid, y, x + 1)
        self.dfs(grid, y -1 , x)
        self.dfs(grid, y, x- 1)
        