class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # run BFS on rotten cells
        # very similar to finding shortest distance to water
        if not grid:
            return -1
        
        ROWS, COLUMNS = len(grid), len(grid[0])
        
        # keep track of the amount of fresh_fruits, so if we don't visit all the fresh_fruits
        # then we know this is impossible
        fresh_fruits = 0
        queue = deque()
        time_elapsed = 0
        
        # traverse the graph, adding rotten fruit to the queue
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_fruits += 1
        # run layer BFS
        while queue and fresh_fruits > 0:
            time_elapsed += 1
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            # explore the current layer (like a graph)
            for i in range(len(queue)):
                y, x = queue.popleft()
                for next_y, next_x in dirs:
                    new_y, new_x = y + next_y, x + next_x
                    if 0 <= new_y < ROWS and 0 <= new_x < COLUMNS and grid[new_y][new_x] == 1:
                        # mark as contaminated and add to the queue
                        fresh_fruits -= 1
                        grid[new_y][new_x] = 2
                        queue.append((new_y, new_x))
        print(fresh_fruits)
        return time_elapsed if fresh_fruits == 0 else -1