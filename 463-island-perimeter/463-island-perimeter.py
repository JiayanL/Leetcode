class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        task: find all edges
        edge condition: when we touch water or the perimeter, we have an edge
        so when we explore and reach either beyond or water, we know that we should add one to the side
        '''
        rows = len(grid)
        columns = len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]
        
        def countEdges(y, x) -> int:

            # condition 1 we've reached perimeter
            if y < 0 or y >= rows or x < 0 or x >= columns:
                return 1

            # condition 2: we've reached water
            if grid[y][x] == 0:
                return 1

            # condition 3: we've visited before
            if visited[y][x] == True:
                return 0

            # condition 4: explore the islands
            edgeCount = 0
            visited[y][x] = True
            
            edgeCount += countEdges(y + 1, x)
            edgeCount += countEdges(y - 1, x)
            edgeCount += countEdges(y, x + 1)
            edgeCount += countEdges(y, x - 1)

            return edgeCount
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return countEdges(i, j)
    