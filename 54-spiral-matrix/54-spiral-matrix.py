class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        # Initialize row beginning and row end
        result = []
        row_start, row_end = 0, len(matrix) - 1
        column_start, column_end = 0, len(matrix[0]) - 1
        
        # Move all the way right, then down, then left, then up
        # Repeat until I've hit the end
        while row_start <= row_end and column_start <= column_end:
            # Move across first row
            for i in range(column_start, column_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1
            
            # Move down last column
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][column_end])
            column_end -= 1
            
            if row_start <= row_end:
                for i in range(column_end, column_start - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1
            
            if column_start <= column_end:
                for i in range(row_end, row_start -1, -1):
                    result.append(matrix[i][column_start])
                column_start += 1
                
        return result