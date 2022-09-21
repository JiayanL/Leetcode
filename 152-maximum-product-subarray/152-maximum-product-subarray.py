class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        result = nums[0]
        max_in_window = nums[0]
        min_in_window = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_in_window * curr, min_in_window * curr)
            min_in_window = min(curr, max_in_window * curr, min_in_window * curr)
            
            max_in_window = temp_max
            result = max(temp_max, result)
            
        return result