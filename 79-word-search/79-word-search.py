class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        WIDTH = len(board[0])
        HEIGHT = len(board)
        
        def backtrack(row, column, match):
            nonlocal board
            # check if I've made a match         
            if len(match) == 0:
                return True
            
            # check if this is valid
            if not 0 <= row < HEIGHT or not 0 <= column < WIDTH or \
            board[row][column] != match[0]:
                return False
            
            # print(row, column)
            #backtrack -> mark this piont as visited and go to all children
            board[row][column] = "#"
            ret = False
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for y, x in dirs:
                ret = backtrack(row + y, column + x, match[1:])
                if ret: break
            board[row][column] = match[0]
            
            return ret
        
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if backtrack(i, j, word):
                    return True
        return False