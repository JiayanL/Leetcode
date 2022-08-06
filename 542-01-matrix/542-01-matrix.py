from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS solution, let's do this one in place
        rows, columns = len(mat), len(mat[0])
        queue = deque()
        nextDir = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # find all zeros
        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 0:
                    queue.append([i, j])
                else:
                    mat[i][j] = -1
            
        # multi source BFS
        while queue:
            i, j = queue.popleft()
            
            for dI, dJ in nextDir:
                newI, newJ = i + dI, j + dJ
                # check that its valid and not visited
                if 0 <= newI < rows and 0 <= newJ < columns and mat[newI][newJ] == -1:
                    mat[newI][newJ] = mat[i][j] + 1
                    queue.append([newI, newJ])
        return mat