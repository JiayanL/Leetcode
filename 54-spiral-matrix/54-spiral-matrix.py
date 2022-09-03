class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        
        result = []
        row_start, row_end = 0, len(matrix) - 1
        column_start, column_end = 0, len(matrix[0]) - 1
        
        # go all the way right, then all the way down, then all the way left, then all the way up
        while row_start <= row_end and column_start <= column_end:
            
            # all the awy right
            for i in range(column_start, column_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1
            
            # all the way down
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][column_end])
            column_end -= 1
            
            # all the way left
            # one more check
            if row_start <= row_end:
                for i in range(column_end, column_start - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1
            
            # all the way up
            if column_start <= column_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][column_start])
                column_start += 1
            
        return result
                        