class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize pointers at the beginning and end of the container
        # track the max
        # loop through the array
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            width = right - left
            max_area = max(max_area, width * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
            
                