class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge cases - empty grid
        if not grid:
            return 0
        count = 0
        # bfs
        # visit every point in the grid
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    grid[y][x] = 0
                    count += 1
                    self.bfs(grid, [y,x])
                    
        return count
    
    def bfs(self, grid, coords) -> None:
        # create a queue
        queue = collections.deque([coords])
        # add all points around it
        while queue:
            y, x = queue.popleft()
            for i, j in [[y + 1, x], [y - 1, x], [y, x + 1], [y, x - 1]]:
                if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j] == "1":
                    queue.append([i,j])
                    grid[i][j] = 0
            
                
        
#     def dfs_iterative(self, grid, coords) -> None:
#         pass
    
#     def dfs_recursive(self, grid, coords) -> None:
#         pass
        