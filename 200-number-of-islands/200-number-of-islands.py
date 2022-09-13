class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        HEIGHT = len(grid)
        WIDTH = len(grid[0])
        
        def bfs(row, column):
            
            moves = [(1,0), (-1,0), (0,1), (0, -1)]
            for y, x in moves:
                newRow, newColumn = row + y, column + x
                if 0 <= newRow < HEIGHT and 0 <= newColumn < WIDTH and grid[newRow][newColumn] == "1":
                    grid[newRow][newColumn] = "#"
                    bfs(newRow, newColumn)
        
        for row in range(HEIGHT):
            for column in range(WIDTH):
                if grid[row][column] == '1':
                    islandCount += 1
                    grid[row][column] = "#"
                    bfs(row, column)
        
        return islandCount