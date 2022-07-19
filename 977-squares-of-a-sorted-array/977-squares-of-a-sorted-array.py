class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = []
        
        while left <= right:
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2
            
            if left_squared > right_squared:
                result.append(left_squared)
                left += 1
            elif right_squared >= left_squared:
                result.append(right_squared)
                right -= 1
    
        return reversed(result)
                
                