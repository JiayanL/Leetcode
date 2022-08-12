class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        
        if not grid:
            return islandCount
        
        rows = len(grid)
        columns = len(grid[0])
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    grid[i][j] = "#"
                    islandCount += 1
                    self.bfs(grid, i, j)
        return islandCount
    
    def bfs(self, grid: List[List[str]], i: int, j: int) -> None:
        queue = collections.deque([(i, j)])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            i, j = queue.popleft()
            for dX, dY in d:
                newX, newY = i + dX, j + dY
                if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == "1":              
                    grid[newX][newY] = "#"
                    queue.append((newX, newY))
