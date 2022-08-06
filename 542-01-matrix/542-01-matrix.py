from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return mat
        
        columns = len(mat[0])
        
        distances = [[float(inf) for _ in range(columns)] for _ in range(rows)]
        
        # traverse right -> down
        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 0:
                    distances[i][j] = 0
                else:
                    if i > 0:
                        distances[i][j] = min(distances[i][j], distances[i - 1][j] + 1)
                    if j > 0:
                        distances[i][j] = min(distances[i][j], distances[i][j - 1] + 1)
                        
        # traverse left -> up
        for i in range(rows - 1, -1, -1):
            for j in range(columns - 1, -1, -1):
                print(j)
                if mat[i][j] == 0:
                    distances[i][j] = 0
                else:
                    if i < (rows - 1):
                        distances[i][j] = min(distances[i][j], distances[i + 1][j] + 1)
                    if j < (columns - 1):
                        distances[i][j] = min(distances[i][j], distances[i][j + 1] + 1)
            
            
        
        return distances