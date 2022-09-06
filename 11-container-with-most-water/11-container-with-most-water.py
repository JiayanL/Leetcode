class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            left_height = height[left]
            right_height = height[right]
            area = min(left_height, right_height) * (right - left)
            max_area = max(max_area, area)
            if right_height < left_height:
                right -= 1
            else:
                left += 1
        return max_area