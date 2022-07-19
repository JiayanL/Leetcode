class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    
        stack = [(sr, sc)]
        color_seek = image[sr][sc]
        m, n = len(image), len(image[0])
        
        if color_seek == color:
            return image
        
        while stack:
            y, x = stack.pop()
            image[y][x] = color

            # add 4 diagonals
            if y + 1 < m and image[y+1][x] == color_seek:
                stack.append((y+1,x))
            if y - 1 >= 0 and image[y-1][x] == color_seek:
                stack.append((y-1,x))
            if x + 1 < n and image[y][x+1] == color_seek:
                stack.append((y,x+1))
            if x - 1 >= 0 and image[y][x-1] == color_seek:
                stack.append((y,x-1))
                
        return image
                
            